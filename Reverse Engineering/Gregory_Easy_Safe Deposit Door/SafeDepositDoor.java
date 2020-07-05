import java.util.*;

class SafeDepositDoor {
    public static void main(String args[]) {
        SafeDepositDoor depositdoor = new SafeDepositDoor();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter deposit door password: ");
	String userInput = scanner.next();
	String input = userInput.substring("YCEP{".length(),userInput.length()-1);
	if (depositdoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
    }

    public boolean checkPassword(String password) {
        return password.length() == 25 &&
               password.charAt(0)  == 'd' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == '1' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(22) == '3' ;

    }
}
