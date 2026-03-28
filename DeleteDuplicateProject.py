# Import required libraries
import hashlib      # Used for generating hash values (MD5) used to identify duplicate files
import os           # Used for file and directory operations remove ,walk ,path


# Function to calculate checksum (hash value) of a file
def CalculateChecksum(FileName):

    # Open file in binary mode to read all file types (text, image, video)
    fobj = open(FileName,"rb")  
    
    # Create MD5 hash object
    hobj = hashlib.md5()
    
    # Read first 1024 bytes of file
    Buffer = fobj.read(1024)        
    
    # Loop until file data ends
    while(len(Buffer) > 0):
        
        # Update hash object with current buffer data
        hobj.update(Buffer)
        
        # Read next 1024 bytes
        Buffer = fobj.read(1024)
        
    # Close the file
    fobj.close()
    
    # Return the final checksum value in hexadecimal format
    return hobj.hexdigest()


# Function to find duplicate files in a directory
def FindDuplicate(DirectoryName="Marvellous"):
    
    Ret = False
    
    # Check whether directory exists
    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("There is No Such Directory")
        return
    
    # Check if the path is actually a directory
    Ret = os.path.isdir(DirectoryName)
    
    if(Ret == False):
        print("It is not a Directory")
        return
    
    # Dictionary to store file checksum and file paths
    Duplicate = {}              
    
    # Traverse directory recursively
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        
        # Iterate through files
        for fname in FileName:
            
            # Create full file path
            fname = os.path.join(FolderName,fname)
            
            # Calculate checksum of the file
            CheckSum = CalculateChecksum(fname)
            
            # If checksum already exists → duplicate file
            if CheckSum in Duplicate:
                
                # Append file path to existing list
                Duplicate[CheckSum].append(fname)
            
            else:
                # Otherwise create new list with this file
                Duplicate[CheckSum] = [fname]
                
    # Return dictionary containing duplicate file info
    return Duplicate


# Function to display duplicate files
def DisplayResult(MyDict):
    
    # Filter only duplicate entries (list length > 1)
    Result = list(filter(lambda x :len(x) > 1 , MyDict.values()))
    
    Count = 0
    
    # Iterate through duplicate groups
    for Value in Result:
        
        for subvalue in Value:
            
            Count = Count + 1
            
            # Print duplicate file path
            print(subvalue)
        
        # Display number of files in this duplicate group
        print("Value of Count is: ",Count)
        
        Count = 0


# Function to delete duplicate files
def DeleteDuplicate(Path = "Marvellous"):
    
    # Get dictionary of duplicate files
    MyDict = FindDuplicate(Path)
    
    # Filter duplicate file lists
    Result = list(filter(lambda x :len(x) > 1 , MyDict.values()))
    
    Count = 0
    Cnt = 0
    
    # Traverse duplicate groups
    for Value in Result:
        
        for subvalue in Value:
            
            Count = Count + 1
            
            # Keep first file and delete remaining duplicates
            if(Count > 1):
                
                print("Deleted File: ",subvalue)
                
                # Delete duplicate file
                os.remove(subvalue)
                
                Cnt = Cnt + 1
        
        Count = 0
    
    # Print total deleted files
    print("Total Deleted File: ",Cnt)
    

# Main function (program entry point)
def main():
    
    # Call function to delete duplicate files
    DeleteDuplicate()


# Execute main function only when script runs directly
if __name__ == "__main__":
    main()