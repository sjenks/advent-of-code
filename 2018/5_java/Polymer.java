import java.util.*;

import javax.sound.midi.MidiEvent;

import java.io.*;

public class Polymer {
    public static void main(String[] args) throws Exception{
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String line = br.readLine();
            Character[] charObjectArray = line.chars().mapToObj(c -> (char)c).toArray(Character[]::new);
            for(char alpha = 'a'; alpha <='z'; alpha++) {
                ArrayList<Character> alphaRemoved = removeLetter(alpha, charObjectArray);
                System.out.print(alpha + " ");
                process(alphaRemoved);
            }
        }
    }

    private static ArrayList<Character> removeLetter(char alpha, Character[] charObjectArray) {
        ArrayList<Character> prunedChars = new ArrayList<Character>();
        for(Character c : charObjectArray) {
            if(Character.toUpperCase(alpha) != Character.toUpperCase(c.charValue())) {
                prunedChars.add(c);
            }
        }
        return prunedChars;
    }

    private static void process(ArrayList<Character> polymer) {
        //List<Character> polymerList = Arrays.asList(polymerArr);
        //ArrayList<Character> polymer = new ArrayList<Character>(polymerList);

        int lastSize = -1;
        do {
            lastSize = polymer.size();
            polymer = removeDuplicates(polymer);
        } while (lastSize != polymer.size());

        System.out.println(polymer.size());
    }

    private static ArrayList<Character> removeDuplicates(ArrayList<Character> polymer) {
        for (int i = 1; i < polymer.size(); i++) {
            Character prevChar = polymer.get(i-1);
            Character curChar = polymer.get(i);
            if(xorCase(prevChar, curChar)) {
                polymer.remove(i);
                polymer.remove(i-1);
                break;
            }
        }
        return polymer;
    }

    private static boolean xorCase(Character left, Character right) {
        char l = left.charValue();
        char r = right.charValue();
        boolean isLeftUpper = Character.isUpperCase(l);
        boolean isRightUpper = Character.isUpperCase(r);

        boolean mixedCase = isLeftUpper ^ isRightUpper;
        boolean sameLetter = (Character.toUpperCase(l) == Character.toUpperCase(r));

        return mixedCase && sameLetter;
    }
}