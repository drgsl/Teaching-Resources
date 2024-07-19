public class Utils {
    public static int[] reverseArray(int[] arr){
        return IntStream.rangeClosed(1, arr.length)
                        .map(i -> arr[arr.length - i])
                        .toArray();
    }
}
