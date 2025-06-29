import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class MultiMark {
    public static void sortRandomList(int size) {
        Random rand = new Random();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(1_000_001);
        }
        Arrays.sort(arr);
    }

    public static double benchmark(int threadCount, int listSize) throws InterruptedException {
        Thread[] threads = new Thread[threadCount];
        long start = System.nanoTime();
        for (int i = 0; i < threadCount; i++) {
            threads[i] = new Thread(() -> sortRandomList(listSize));
            threads[i].start();
        }
        for (Thread t : threads) {
            t.join();
        }
        long end = System.nanoTime();
        return (end - start) / 1e9;
    }

    public static void main(String[] args) throws Exception {
        int cpuCores = Runtime.getRuntime().availableProcessors();
        System.out.println("CPU cores: " + cpuCores);
        int[] threadCounts = {1, 2, 4, 8, 16, 32, 64};
        List<Double> times = new ArrayList<>();
        int listSize = 1_000_000;

        for (int n : threadCounts) {
            double t = benchmark(n, listSize);
            System.out.printf("Threads: %d, Time taken: %.4f seconds%n", n, t);
            times.add(t);
        }

        // Print results as CSV for external plotting
        System.out.println("\nThreadCount,TimeTakenSeconds");
        for (int i = 0; i < threadCounts.length; i++) {
            System.out.printf("%d,%.6f%n", threadCounts[i], times.get(i));
        }
    }
}
