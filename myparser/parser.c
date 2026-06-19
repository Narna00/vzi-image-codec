#include <Python.h>
#include <string.h>

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

    // Vulnerable fixed-size buffer
    char buffer[64];

    // No bounds check – overflow if size > 64
    memcpy(buffer, data, size);

    // Return a bytes object to prevent optimization
    Py_ssize_t ret_size = size < 64 ? size : 64;
    return PyBytes_FromStringAndSize(buffer, ret_size);
}

static PyMethodDef methods[] = {
    {"parse", parse, METH_VARARGS, "Parse input data"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "parser",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_parser(void) {
    return PyModule_Create(&module);
}
