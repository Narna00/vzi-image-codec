import ctypes
import struct

def parse_vzi(data: bytes) -> bool:
    if len(data) < 8:
        return False
        
    # Header: Magic bytes (VZI\x00), Width (2 bytes), Height (2 bytes)
    magic, width, height = struct.unpack('<4sHH', data[:8])
    if magic != b'VZI\x00':
        return False
        
    if width == 0 or height == 0 or width > 512 or height > 512:
        return False
        
    total_pixels = width * height
    # Allocate explicit native heap memory block
    raw_buffer = ctypes.create_string_buffer(total_pixels)
    base_ptr = ctypes.cast(raw_buffer, ctypes.c_void_p).value
    
    idx = 8
    buf_idx = 0
    
    while idx < len(data):
        cmd = data[idx]
        idx += 1
        
        if cmd == 0xFF: # Relative buffer seek command
            if idx + 2 > len(data):
                break
            offset = struct.unpack('<h', data[idx:idx+2])[0] # Signed short
            idx += 2
            
            # VULNERABILITY: Missing lower-bound validation (buf_idx + offset < 0)
            if buf_idx + offset >= total_pixels:
                continue
            buf_idx += offset
            continue
            
        # Write operations: upper bit determines mode, lower 7 bits equal chunk length
        mode = (cmd & 0x80) >> 7
        length = cmd & 0x7F
        
        if length == 0:
            continue
            
        if buf_idx + length > total_pixels:
            break
            
        if mode == 0: # Literal block write
            if idx + length > len(data):
                break
            for _ in range(length):
                # Out-of-bounds memory write occurs here if buf_idx is negative
                ctypes.memset(base_ptr + buf_idx, data[idx], 1)
                idx += 1
                buf_idx += 1
        else: # Repeat block write
            if idx >= len(data):
                break
            val = data[idx]
            idx += 1
            for _ in range(length):
                ctypes.memset(base_ptr + buf_idx, val, 1)
                buf_idx += 1
                
    return True