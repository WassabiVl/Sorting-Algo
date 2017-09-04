<?php
$a = [3,56,8657,56756,567,5675,65,6756];
// @todo write a function which sorts any given array with numeric values (as for axample $a). 
// Do not use existing PHP implementations which would do this job in a single line, but make use of basic algorithmic structures. 
// code goes here
function insertSortFun(array $arlist) //uses the insertion sort function method for its easy and quick implemntation with small arrays
{   // step 1, loop through the array
	for($i=0;$i<count($arlist);$i++) 
	{ //step 2 call the variables to be used
		$val = $arlist[$i]; //call the array item according to the loop
		$j = $i-1;// call the perivous array item
		while($j>=0 && $arlist[$j] > $val)//loop to through slected values and compares the last value to the previous
		{
			$arlist[$j+1] = $arlist[$j]; //swaps the location of the values
			$j--; //to move back through the array
		}
		$arlist[$j+1] = $val; //optimized method to swap last value
	}
return $arlist;
}
print_r(insertSortFun($a));
>