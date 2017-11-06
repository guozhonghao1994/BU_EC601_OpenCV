'''
The general form of CvMat is: CV_(S|U|F)C.
CvMat* cvCreateMat (int rows, int cols, int type);
Bit depth can be 8, 16, 32 or 64 bits. This is the amount of memory for the single orange cell in the above picture.
S means signed integer, U means unsigned integer and F means floating point (decimal values)
You can have any number of channels
Thus, CV_8UC3 is for 8 bit unsigned integer matrices with 3 channels. CV_32SC2 is for 32 bit signed integer matrices with 2 channels. CV_64FC1 is for 64 bit floating point matrices with a single channel.

Internally, the CvMat structure looks like this:
'''
typedef struct CvMat
{
    int type;
    int step;

    int* refcount; /* underlying data reference counter */

    union
    {
        uchar* ptr;
        short* s;
        int* i;
        float* fl;
        double* db;

    } data;

    int rows;
    int cols;
} CvMat;