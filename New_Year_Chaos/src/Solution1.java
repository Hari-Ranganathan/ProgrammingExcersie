import java.net.Inet4Address;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Solution1 {

    public static void minimumBribes(List<Integer> q){
//        List<Integer> ordered = q.stream().sorted().collect(Collectors.toList());
//        System.out.println(q);
//        System.out.println(ordered);
//        int len = q.size(), count = 0;
//        boolean isChaotic = false;
//        for(int i=0; i < len; i++){
//            if(isChaotic == false) {
//                for (int j = 0; j < len; j++) {
//                    if (q.get(i) == ordered.get(j)) {
//                        int positionDifference = 0;
//                        positionDifference = j - i;
//                        System.out.println("positionDifference " + positionDifference);
//                        if (positionDifference > 2) {
//                            isChaotic = true;
//                            break;
//                        } else if (positionDifference > 0) {
//                            count += positionDifference;
//                            break;
//                        }
//                    }
//                }
//            }
//        }
//        if(isChaotic){
//            System.out.println("Too Chaotic");
//        }else{
//            System.out.println(count);
//        }
        int len = q.size(), result = 0;
        for(int i = len -1; i >= 0; i--){
            int changedPosition = q.get(i) - (i + 1);
            if(changedPosition > 2){
                System.out.println("Too Chaotic");
                return;
            }else{
                int index = Math.max(0, q.get(i)-2);
                for(int j = index; j < i; j++){
                    if(q.get(j) > q.get(i)) result++;
                }
            }
        }
        System.out.println(result);
    }

    public static void main(String[] args) {
        List<Integer> array1 = new ArrayList<>();
        //int[] arr = new int[]{2, 1, 5, 3, 4}; //+ve case 1 Pass
        int[] arr = new int[]{1, 2, 5, 3, 7, 8, 6, 4}; //+ve case 2 Fail
        //int[] arr = new int[]{1, 2, 5, 3, 4, 7, 8, 6}; //+ve case 3 Pass
        //int[] arr = new int[]{2, 5, 1, 3, 4}; //-ve Case 1 Pass
        //int[] arr = new int[]{5, 1, 2, 3, 7, 8, 6, 4}; // -ve case 2 Pass
        for(int i =0; i < arr.length; i++){
            array1.add(arr[i]);
        }
        Solution1.minimumBribes(array1);
    }
}
