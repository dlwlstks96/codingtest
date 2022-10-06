import java.util.Arrays;
import java.util.List;

class Solution {
    public int solution(String s) {
        int answer = 0;

        String tmpAnswer = "";

        String[] nums = s.split("");

        String[] numList = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        String[] strList = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        List<String> newNumList = Arrays.asList(numList);
        List<String> newStrList = Arrays.asList(strList);

        //System.out.println(nums[1]);

        String tmpStr = "";

        for (String n : nums) {
            //System.out.println(n + " / " + tmpStr);

            if (newStrList.contains(tmpStr)) {
                tmpAnswer += numList[newStrList.indexOf(tmpStr)];
                tmpStr = "";
            }

            if (newNumList.contains(n)) {
                tmpAnswer += n;
            } else {
                tmpStr += n;
            }


        }

        if (!tmpStr.equals("")) {
            tmpAnswer += numList[newStrList.indexOf(tmpStr)];
        }

        //System.out.println(tmpAnswer);

        answer = Integer.valueOf(tmpAnswer);

        return answer;
    }
}
