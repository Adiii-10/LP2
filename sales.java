public class selection {
     // method to perform selection sort
    public static List<Integer> selectionSort(List<Integer> arr) {
        Integer n = arr.size();

        for (Integer i = 0; i < n; i++) {
            Integer minIndex = i;

            // find minimum element
            for (Integer j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // swap elements
            Integer temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }

        return arr;
    }
     

}


// Create a list
List<Integer> nums = new List<Integer>{64, 25, 12, 22, 11};

// Call your method
List<Integer> sortedList = selection.selectionSort(nums);

// Print output
System.debug('Sorted List: ' + sortedList);
