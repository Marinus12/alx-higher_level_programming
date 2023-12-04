#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python list
 * @p: A Pyobject list
 */
void print_python_list_info(PyObject *p)
{
        int size, alloc, j;
        PyObject *obj;

        size = Py_SIZE(p);
        alloc = ((PyListObject *)p)->allocated;
        printf("[*] Size of the python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);
        for (j = 0; j < size; j++)
        {
                printf("Element %d: ", j);
                obj = PyList_GetItem(p, j);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}
