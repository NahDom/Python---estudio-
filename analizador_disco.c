#define _XOPEN_SOURCE 500 //tal parece es alguna funcion de pruebas...
#include <stdio.h>
#include <ftw.h>
#include <stdlib.h>
#include <math.h>
#define PATH_MAX_SIZE 4096
// uso un arreglo para almacenar el tamaño de los archivos
typedef struct 
{
    char path[PATH_MAX_SIZE];
    size_t size;
}FileEntry;

// arreglo de archivos
FileEntry *files;

size_t current_index = 0;
size_t current_capacity = 10;
int function(const char *path, const struct stat *sb, int typeflag, struct FTW *ftwbuf)
{   
    if (typeflag == FTW_DNR || typeflag == FTW_NS){
        return 0; // si el tipo de archivo es un directorio no legible o un archivo que no se puede acceder, se omite y se continúa con el siguiente archivo
    }
    if (typeflag != FTW_F){
        return 0; // si el tipo de archivo no es un archivo regular, se omite y se continúa con el siguiente archivo
    }
    // verifico si quedo sin espacio en el arreglo de memoria, de ser asi debe de reasignar memoria para el arreglo de archivos, esto es necesario porque no se sabe cuantos archivos hay en el disco
    if(current_index >= current_capacity){
        current_capacity *= 2; // duplico la capacidad del arreglo, ya que esto es una estrategia común para manejar arreglos dinámicos, al duplicar la capacidad se reduce la cantidad de veces que se necesita reasignar memoria a medida que se agregan más archivos
    
        FileEntry *temp = realloc(files, current_capacity * sizeof(FileEntry)); 
        //realloc es una función que se utiliza para cambiar el tamaño de un bloque de memoria previamente asignado. En este caso, se está utilizando para aumentar la capacidad del arreglo de archivos. Si realloc no puede asignar la nueva cantidad de memoria, devuelve NULL, por lo que es importante verificar si temp es NULL antes de actualizar el puntero files

        if (temp == NULL){
            perror("fallo al resaignar memoria");
            exit(-1);
        }
        files = temp; // actualizo el puntero al nuevo bloque de memoria
    }

    size_t filesize = sb->st_size;
    strncpy(files[current_index].path, path, PATH_MAX_SIZE - 1);
    files[current_index].path[PATH_MAX_SIZE -1] = '\0'; // aseguro que la cadena esté terminada en null
    files[current_index].size = filesize;

    current_index++;
    return 0;
}  

void init_files()
{
    files = (FileEntry *) calloc(10, sizeof(FileEntry));
    if (files == NULL){
        perror("el arreglo de archivos no puede encontrarse");
        exit(-1);
    }
}

int sort(const void *first, const void *second){
    FileEntry uno = *(FileEntry *) first;
    FileEntry dos = *(FileEntry *) second;

    if (uno.size == dos.size)
        return 0;
    if (uno.size > dos.size)
        return -1;
    if (uno.size < dos.size)
        return 1;  
}

size_t find_max_filesize(){
    size_t current_max = 0;
    for (size_t i= 0; i <current_index; i++){
        // aqui se compara el tamaño de cada archivo con el tamaño máximo actual, si el tamaño del archivo es mayor que el tamaño máximo actual, se actualiza el tamaño máximo con el tamaño del archivo. Al finalizar el ciclo, current_max contendrá el tamaño del archivo más grande encontrado en el arreglo de archivos
        if (files[i].size > current_max){
            current_max = files[i].size;
        }
    }
    return current_max;
}
void print_files(){
    size_t max = find_max_filesize();
    for(size_t i = 0; i < current_index; i++)
    {
        int num_blocks = log10(((float) files[i].size) / log10((float) max));
        for (int j = 0; j < num_blocks; j++){
            printf("#");    
    }
        for ( int j = num_blocks; j < 20; j++){
            printf("");
        }
        double size_in_mb = (double)files[i].size / (1024*1024);
        printf("\t%10.2f MB \t%s\n",size_in_mb, files[i].path);
    }
}
// funcion para imprimir los archivos y su tamaño

/*void print_files()
{
    for (size_t i = 0; i < current_index; i++)
    {
        printf("Ruta: %s\nTamanio: %ld\t", files[i].path, files[i].size);
    }
}
*/
void liberar_memoria()
{
    //funcion para liberar la memoria del arreglo de archivos, esto me permite evitar fugas de memoria
    // de modo que al finalizar el programa se libera la memoria asignada para el arreglo de archivos
    free(files);
}

int main(){
    printf("El uso de tu disco es: \n");

    init_files();
    if (nftw(".", function, 15, FTW_PHYS) == -1){
        perror("Error leyendo el arbol de directorios");
    };

    qsort(files, current_index, sizeof(FileEntry), sort);
    print_files();
    liberar_memoria();
    return 0;
}