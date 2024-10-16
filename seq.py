#given the sequence
sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

#function to split the sequence into chunks of 20 letters and write each
#chunk to a seperate file

def split_sequence_to_files(sequence, chunk_size=20):
        for i in range(0, len(sequence), chunk_size):
            chunk = sequence[i:i+chunk_size]

            with open(f"chunk_{i//chunk_size + 1}.txt","w") as f:
                f.write(f"{chunk}\n")



#call the fnction to split the sequence and write to files

split_sequence_to_files(sequence)


 
