static PyObject* parse(PyObject* self, PyObject* args) {
    PyObject* data_obj;
    if (!PyArg_ParseTuple(args, "O", &data_obj))
        return NULL;
    if (!PyBytes_Check(data_obj)) {
        PyErr_SetString(PyExc_TypeError, "Expected bytes");
        return NULL;
    }
    const char* data = PyBytes_AsString(data_obj);
    Py_ssize_t size = PyBytes_Size(data_obj);

    // ---- ADD THIS BOUNDS CHECK ----
    if (size > 64) {
        PyErr_SetString(PyExc_ValueError, "Input size exceeds buffer capacity");
        return NULL;
    }
    // ------------------------------

    // Vulnerable fixed-size buffer
    char buffer[64];

    // No bounds check – overflow if size > 64
    memcpy(buffer, data, size);

    // Return a bytes object to prevent optimization
    Py_ssize_t ret_size = size < 64 ? size : 64;
    return PyBytes_FromStringAndSize(buffer, ret_size);
}
