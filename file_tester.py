# Imports
import time
import encryption
import compression

read_counter = 10
# File comparison method (checks for errors in each line of output file by comparing to input file)
def file_comparison(fileName1, fileName2):
    original_file = open(fileName1, "r")  
    received_file = open(fileName2, "r")  
  
    line_error_count = 0
  
    for original_line in original_file:

        for received_line in received_file:
          
            # Comparing same line numbers from each file
            if original_line == received_line:  
                line_error_count += 0
            else:
                line_error_count += 1       
            break
  
    original_file.close()                                       
    received_file.close()

    return line_error_count

# ON THE SENDING END:

# Start the operations timer for testing purposes
subsys_start_time = time.time()
print("\nPerforming operations on the data: Results pending...")

# First, compress the raw data from the input .csv file
input_file_path = "RT_IMU_Data/Data_Set_" + str(read_counter) + "_Mins.csv"
print("\n------------------------------------------------------------------")
print("Compressing the data...")
compression.myCompress(input_file_path)
print("\nCompression successful.")
print("------------------------------------------------------------------")

# Encrypt the compressed data file
print("Encrypting the data...")
encryption.encrypt_data('Compressed_Files/Compressed_Data_' + str(read_counter) + '_Mins.csv')
print("\nEncryption successful.")
print("------------------------------------------------------------------")
        
# ON THE RECEIVING END NOW:

# Decrypt the data file
print("Decrypting the data...")
encryption.decrypt_data('Encrypted_Files/Encrypted_Data_' + str(read_counter) + '_Mins.csv')
print("\nDecryption successful.")
print("------------------------------------------------------------------")

# Decompress the decrypted data file  
print("Decompressing the data...")
compression.myDecompress('Decrypted_Files/Decrypted_Data_' + str(read_counter) + '_Mins.csv')
print("\nDecompression successful.")
print("------------------------------------------------------------------")

# Stop the timer
total_subsys_time = time.time() - subsys_start_time

# Do data loss check between input and output files
input_file = 'RT_IMU_Data/Data_Set_' + str(read_counter) + '_Mins.csv'
output_file = 'Decompressed_Files/Decompressed_Data_' + str(read_counter) + '_Mins.csv'
data_loss_count = file_comparison(input_file, output_file) # file_comparison method written above

print("Overall Results:")
print("- Total time taken for all operations was " + str(round(total_subsys_time, 3)) + " seconds (no transmission time accounted for).")
print("- Data loss detection tests found that there were " + str(data_loss_count) + " differences between the input and output files.")
print("\nNote: The output .csv file is contained inside the 'Decompressed_Files' folder.")
print("------------------------------------------------------------------")
