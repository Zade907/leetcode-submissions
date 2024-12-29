
public class Solution {
    public int FindClosestNumber(int[] nums) { // bk
        int closestNumToZero = nums[0]; // closest number to zero

        int distanceToZero1 = nums[0] > 0 ? nums[0] : nums[0] * -1; // temp placeholder to hold closest number to zero

        for (int i = 0; i < 1000 && i< nums.Length; i++)
        {
            int distanceToZero2 = nums[i] > 0 ? nums[i] : nums[i] * -1;
            
            if((distanceToZero2 < distanceToZero1) || ((distanceToZero2 == distanceToZero1) && nums[i] > 0))
            {
                closestNumToZero = nums[i];
                distanceToZero1 = distanceToZero2;
            }
        }

        return closestNumToZero;
    }

    /*public int FindClosestNumberRK(int[] nums) {
        // int smallestnum = int.minValue;
        int closestnum = 0;//int.minValue;

        for(int i =0; i< nums.Length; i++)
        {
            int temp=0;
            int temp2 =0;
        
            if(i==0)
                closestnum = nums[i];
            else
            {
                if(nums[i] < 0) // negative numbers
                   temp = nums[i] * -1;
                if(closestnum < 0) // negative numbers
                   temp2 = closestnum * -1;
                if(0-temp > 0-temp2)
                    closestnum = nums[i];
            }          

        }
      // Console.WriteLine(closestnum);
        return closestnum;
    }*/
}
