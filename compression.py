# Imports
import zlib
import sys
import time

global current_count
current_count = 10

# Compression method, takes the input file as its input parameter
def myCompress (inputFile):
    # Start timer for compression testing purposes
    compress_start = time.time()

    with open(inputFile, mode="rb") as fin, open("Compressed_Files/Compressed_Data_" + str(current_count) + "_Mins.csv", mode="wb") as fout:
        data = fin.read()
        compressed_data = zlib.compress(data, 1)
        
        # Display the file sizes before and after compression, for testing purposes
        print("\nCompression Results:")
        print(f"- Input file size: {sys.getsizeof(data)} bytes (or " + str(round(sys.getsizeof(data)/100000, 5)) + " MB).")
        print(f"- Compressed file size: {sys.getsizeof(compressed_data)} bytes (or " + str(round(sys.getsizeof(compressed_data)/100000, 5)) + " MB).")
        print(f"- The compression ratio was: " + str(round(sys.getsizeof(data)/sys.getsizeof(compressed_data), 3)) + ".")

        fout.write(compressed_data)
    
    compress_time_taken = time.time() - compress_start
    print("- Compression: It took " + str(round(compress_time_taken, 3)) + " seconds to read in, compress, and return the data.")

# Decompression method, takes the decrypted compressed file as input
def myDecompress (compressedFile):
    # Start timer for decompression testing purposes
    decompress_start = time.time()
    
    with open(compressedFile, mode="rb") as fin, open("Decompressed_Files/Decompressed_Data_" + str(current_count) + "_Mins.csv", mode="wb") as fout:
        data = fin.read()
        decompressed_data = zlib.decompress(data)
        
        # Display the file sizes before and after decompression, also to be compared with file sizes displayed in the compression sub-subsystem
        print("\nDecompression Results:")
        print(f"- Compressed file size: {sys.getsizeof(data)} bytes (or " + str(round(sys.getsizeof(data)/100000, 5)) + " MB).")
        print(f"- Decompressed file size: {sys.getsizeof(decompressed_data)} bytes (or " + str(round(sys.getsizeof(decompressed_data)/100000, 5)) + " MB).")

        fout.write(decompressed_data)
    
    # Stop the decompression timer
    decompress_time_taken = time.time() - decompress_start
    print("- Decompression: It took " + str(round(decompress_time_taken, 3)) + " seconds to read in, decompress, and return the data.")
    print("\nPlease see the data loss test results below.")