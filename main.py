# Imports
import time
import encryption
import compression

# SENDING END (ON SHARC BUOY):

# Get input and output .csv file names
input_csv_name = input("Enter the name of the .csv file containing the data:\n")

# Start the timer for testing purposes
start_time = time.time()
print("\nPerforming operations on the data: Results pending...")

# First, compress the raw data from the input .csv file
input_file_path = "IMU_Data/" + input_csv_name + ".csv"
print("\n------------------------------------------------------------------")
print("Compressing the data...")
compression.myCompress(input_file_path)
print("\nCompression successful.")
print("------------------------------------------------------------------")

# Encrypt the compressed data file
print("Encrypting the data...")
encryption.encrypt_data('Compressed_Files/Compressed_Data.csv')
print("\nEncryption successful.")
print("------------------------------------------------------------------")

# ON THE RECEIVING END NOW:

# Decrypt the data file
print("Decrypting the data...")
encryption.decrypt_data('Encrypted_Files/Encrypted_Data.csv')
print("\nDecryption successful.")
print("------------------------------------------------------------------")

# Decompress the decrypted data file
print("Decompressing the data...")
compression.myDecompress('Decrypted_Files/Decrypted_Data.csv')
print("\nDecompression successful.")
print("------------------------------------------------------------------")

# Stop the timer
total_time_taken = time.time() - start_time
print("Overall Results:")
print("Total time taken for all operations was " + str(round(total_time_taken, 3)) + " seconds (no transmission time accounted for).")
print("\nNote: The output .csv file is contained inside the 'Decompressed_Files' folder.")
print("------------------------------------------------------------------")
