# Imports
import time
import encryption
import compression

# SENDING END (ON SHARC BUOY):

# Get input and output .csv file names
input_csv_name = input("Enter the name of the .csv file containing the data:\n")

# Start the timer for testing purposes
start_time = time.time()

# First, compress the raw data from the input .csv file
compression.myCompress(input_csv_name)

# Encrypt the compressed data file
encryption.encrypt_data('Project Folder\Compressed Files\compressed_data1.csv')

# ON THE RECEIVING END NOW:

# Decrypt the data file
encryption.decrypt_data('Project Folder\Encrypted Files\encrypted_data1.csv')

# Decompress the decrypted data file
compression.myDecompress('Project Folder\Decrypted Files\decrypted_data1.csv')

# Stop the timer
total_time_taken = time.time() - start_time
print("Total time taken for all operations was " + str(round(total_time_taken, 3)) + " seconds (no transmission time accounted for).")