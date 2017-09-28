/*
g++ -std=c++11 -pthread cpp11_threads.cpp
*/
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mut;
int count;

// This function will be called from a thread   
// It counts the occurances of multiples of d between a and b
void call_from_thread(int d, int a, int b) {
	//int temp = 0;
	for (int i = a; i < b; i++)
	{
		if (i % d == 0)
		{
			//temp++;
			count++;
			/*mut.lock();
			count++;
			mut.unlock();
			*/
		}
	}
	//count += temp;
}

int main() {
	int d = 2;
	int range = 100000;
	int thread_count = 5;
	std::thread* my_threads[thread_count];
	
	for (int i = 0; i < thread_count; i++)
	{
		int a = i * range/thread_count;
		int b = (i+1) * range/thread_count;
		std::cout << "For thread #" << i << ", range: (" << a << ", " << b << ")" << std::endl;
		my_threads[i] = new std::thread(call_from_thread, d, a, b);
	}
	
	for (int i = 0; i < thread_count; i++)
		my_threads[i]->join();

	std::cout << std::endl << count << " multiples of " << d << " between 0 and " << range << std::endl;

	return 0;
}