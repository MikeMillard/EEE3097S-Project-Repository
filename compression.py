# Imports
import zlib
import sys
import time

compressedFile = "Project Folder\Compressed Files\compressed_data1.csv"
decompressedFile = "Project Folder\Decompressed Files\decompressed_data1.csv"

# Compression method, takes the input file as its input parameter
def myCompress (inputFile):
    # Start timer for compression testing purposes
    compress_start = time.time()

    with open(inputFile, mode="rb") as fin, open(compressedFile, mode="wb") as fout:
        data = fin.read()
        compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        
        # Display the file sizes before and after compression, for testing purposes
        print("\nCompression:")
        print(f"- Input file size: {sys.getsizeof(data)} bytes.")
        print(f"- Compressed file size: {sys.getsizeof(compressed_data)} bytes.")

        fout.write(compressed_data)
    
    compress_time_taken = time.time() - compress_start
    print("- It took " + str(round(compress_time_taken, 3)) + " seconds to read in, compress, and return the data.")

# Decompression method, takes the decrypted compressed file as input
def myDecompress (compressedFile):
    # Start timer for decompression testing purposes
    decompress_start = time.time()
    
    with open(compressedFile, mode="rb") as fin, open(decompressedFile, mode="wb") as fout:
        data = fin.read()
        decompressed_data = zlib.decompress(data)
        
        # Display the file sizes before and after decompression, also to be compared with file sizes displayed in the compression sub-subsystem
        print("\nDecompression:")
        print(f"- Compressed file size: {sys.getsizeof(data)} bytes.")
        print(f"- Decompressed file size: {sys.getsizeof(decompressed_data)} bytes.")

        fout.write(decompressed_data)
    
    # Stop the decompression timer
    decompress_time_taken = time.time() - decompress_start
    print("- It took " + str(round(decompress_time_taken, 3)) + " seconds to read in, decompress, and return the data.")