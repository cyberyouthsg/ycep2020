import java.util.*;

class File{
    public static void main(String args[]) {
        try{
            File test = new File();
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter password: ");
            String userInput = scanner.next();
            String input = userInput.substring("YCEP{".length(), userInput.length()-1);
            if (test.checkPassword(input)) {
                System.out.println("\nAccess granted.");
            } else {
                System.out.println("\nAccess denied!");
            }
        }catch(Exception e){
            System.out.println("\nAccess denied!");    
        }
    }

    public boolean checkPassword(String password){
        if(password.length() != (770/55)){
            return false;
        }
        byte[] passwordBytes = {
            0x55, 0x6a, 0x32, 0x44, 0x67, 0x56, 
            0x11, 0x40, 0x70, 0x44, 0x21, 0x56, 0x32, 0x76,
            0x66, 0x77, 0x24, 0x23, 0x2a, 0x41, 0x56, 0x66,
            0x6f, 0x52, 0x2e, 0x5f, 0x4f, 0x5f, 0x2a, 0x29,
            0x76, 0x69, 0x69, 0x69, 0x44, 0x33, 0x22, 0x35,
            0x79, 0x28, 0x35, 0x43, 0x40,
            0x5f, 0x2e, 0x5f, 0x4f, 0x5f, 0x2a, 0x65, 0x33, 
            0x22, 0x11, 0x40, 0x40, 0x40, 0x22, 0x43, 0x2a, 0x41,
            0x73, 0x73, 0x69, 0x44, 0x33, 0x22, 0x79, 0x59,
            0x77, 0x37, 0x65, 0x69, 0x69, 0x21, 0x5f, 0x2a, 
            0x65, 0x33, 0x12, 0x21, 0x56, 0x21, 0x55, 0x70, 0x67, 0x77
        };
        byte[] yourBytes = password.getBytes();
        int y = 0;
        String passwordByte = new String(passwordBytes);
        for (int i = 3; i < 86; i += 8){
            i -= 2;
            if(passwordByte.charAt(i) != password.charAt(y)){
                return false;
            }
            y++;
        }
        return true;
    }
}