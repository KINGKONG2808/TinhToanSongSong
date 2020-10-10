program MainQuickSort
    !implicit none
    use omp_lib
    integer a(15)
    a(1)=21
    a(2)=26
    a(3)=5
    a(4)=21
    a(5)=19
    a(6)=17
    a(7)=4
    a(8)=19
    a(9)=26
    a(10)=7
    a(11)=7
    a(12)=2
    a(13)=8
    a(14)=5
    a(15)=8

    print*,"Mang dau vao la:"
    print*,a
    print*
    call omp_set_num_threads(2)
    call QuickSort(a,1,15)
    print*,"Mang da sap xep la:"
    print*,a
end program MainQuickSort
recursive subroutine QuickSort(a,first,last)
    !implicit none
    use omp_lib
	integer a(8),mid,tg
	integer first,last
	integer i,j
    if(first>last) then
        else
	mid = a((first+last)/2)
	i = first;
	j = last
	do while(i<=j)
		do while (a(i)<mid)
			i=i+1
		end do
		do while (mid<a(j))
			j=j-1
		end do
        if(i<=j) then
                tg=a(i)
                a(i)=a(j)
                a(j)=tg
                i=i+1
                j=j-1
        end if
	end do
    !$omp parallel
        !$omp sections
            !$omp section
                call MQuickSort(a,first,j)
            !$omp section
                call MQuickSort(a,i,last)
        !$omp end sections
    !$omp end parallel
    end if
end subroutine QuickSort
recursive subroutine MQuickSort(a,first,last)
    use omp_lib
	integer a(15),mid,tg
	integer first,last
	integer i,j
    print*, 'THREAD',omp_get_thread_num()
    if(first>last) then

    else
	mid = a((first+last)/2)
	i = first;
	j = last
	do while(i<=j)
		do while (a(i)<mid)
			i=i+1
		end do
		do while (mid<a(j))
			j=j-1
		end do
        if(i<=j) then
                tg=a(i)
                a(i)=a(j)
                a(j)=tg
                i=i+1
                j=j-1
        end if
	end do
            call MQuickSort(a,i,last)
            call MQuickSort(a,first,j)
    end if
end subroutine MQuickSort



