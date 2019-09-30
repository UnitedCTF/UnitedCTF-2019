#define PY_SSIZE_T_CLEAN
#include <stdio.h>
#include <python3.6/Python.h>

static PyObject* hackme_cookie(PyObject* self, PyObject* args) {
    const char c[16];
    printf("Here's a cookie for you: %02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx\n", c[24], c[25], c[26], c[27], c[28], c[29], c[30], c[31]);
    fflush(stdout);
    Py_RETURN_NONE;
}

static PyObject* hackme_obfuscate(PyObject* self, PyObject* args) {
    const char* string;
    int length;

    if(!PyArg_ParseTuple(args, "s*i", &string, &length)) {
        return NULL;
    }

    char obfuscated[1024] = {0};
    int escape = 0;

    for(int i = 0; i < length; i++) {
        char c = string[i];
        obfuscated[i] = c ^ 0x04;
    }

    return PyBytes_FromString(obfuscated);
}

static PyMethodDef HackMeMethods[] = {
    {"cookie",  hackme_cookie, METH_VARARGS, "Nom nom nom."},
    {"obfuscate",  hackme_obfuscate, METH_VARARGS, "Obfuscate a string."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef HackMeModule = {
    PyModuleDef_HEAD_INIT,
    "hackme",
    NULL,
    -1,
    HackMeMethods
};

PyMODINIT_FUNC PyInit_hackme(void) {
    return PyModule_Create(&HackMeModule);
}