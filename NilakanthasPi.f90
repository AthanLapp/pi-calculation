Program NilakanthaPi

   integer(8) :: i = 1, pre = 1, calc   
   real(16) :: start = 3, cont = 0

   print*, 'Give me desired calculation limit:'
   read *, calc
   
   do while (i < calc)       
      cont=(i+1)*(i+2)*(i+3)
      start=start+4/cont*pre
      pre=pre*(-1)
      i=i+2
   end do 

   print*, 'Pi calculation using Nilakantha series, with ',  calc, ' number of iterations, gives: ', start

end program