import java.io.*;
import java.net.URL;

public class Main {

    public static final String VOLTRON_TXT = "https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt";

    public static void main(String[] args) throws Exception {
        System.out.println("~~~~~Starting up~~~~~");

        doThing(true);

        System.out.println("~~~~~Finishing up~~~~~");
    }

    public static void doThing(boolean shouldFilter) throws Exception {
        URL url = new URL(VOLTRON_TXT);
        BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()));
        if (shouldFilter) {
            filteredResult(reader);
        } else {
            fullList(reader);
        }
        reader.close();
    }

    public static void filteredResult(BufferedReader reader) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("voltron-pve-filter.txt"));
        String line;
        boolean foundPvp = false;
        while ((line = reader.readLine()) != null) {
            String lower = line.toLowerCase();
            // look for pvp
            if (!foundPvp && lower.contains("pvp") && !lower.contains("pve")) {
                foundPvp = true;
            } else if (line.equals("")) {
                writer.flush();
                foundPvp = false;
            }

            if (!foundPvp) {
                writer.write(line + "\n");
            }
        }
        writer.close();
    }

    public static void fullList(BufferedReader reader) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("voltron.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
                writer.write(line + "\n");
        }
        writer.close();
    }
}