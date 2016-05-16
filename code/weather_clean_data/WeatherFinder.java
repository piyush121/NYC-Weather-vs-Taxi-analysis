import java.io.*;
import java.util.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class WeatherFinder{
    private static HashMap<String, HashSet<String>> mymap = new HashMap<>();
    private static HashMap<String, List<String>> consolidatedWeatherMap = new HashMap<>();
    private static List<String> consolidatedWeatherList = new ArrayList<>();
    private static List<String> normalWeatherList = new ArrayList<>();
    private static List<String> moderateRainList = new ArrayList<>();
    private static List<String> severeRainList = new ArrayList<>();
    private static List<String> moderateSnowList = new ArrayList<>();
    private static List<String> severeSnowList = new ArrayList<>();
    private static List<String> moderateothersList = new ArrayList<>();
    private static List<String> severeothersList = new ArrayList<>();
    private static int numOfLines = 0;
    public static void main(String[] args){
        String fileToRead = "/home/kashishdua/Downloads/Big Data project/weather-data.txt";
        String fileToWrite = "/home/kashishdua/Downloads/Big Data project/consolidated-weather-data.txt";

        try {
            File fileRead = new File(fileToRead);
            FileReader fileReader = new FileReader(fileRead);

            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line;
            String delimiter = " ";

            while ((line = bufferedReader.readLine()) != null) {
                numOfLines++;
                StringTokenizer myline = new StringTokenizer(line, " ");

                int count = 0;
                while(count<2){
                    myline.nextToken();
                    count++;
                }

                String period = myline.nextToken();
                char[] temp = new char[4];
                period.getChars(0,4,temp,0);
                String year = String.valueOf(temp);

                temp = new char[2];
                period.getChars(4,6,temp,0);
                String month = String.valueOf(temp);

                temp = new char[2];
                period.getChars(6,8,temp,0);
                String date = String.valueOf(temp);

                temp = new char[2];
                period.getChars(8,10,temp,0);
                String hour = String.valueOf(temp);

                String finalDate = year+"-"+month+"-"+date+" "+hour+":00";
                //System.out.println(finalDate);

                while(count<11) {
                    myline.nextToken();
                    count++;
                }

                HashSet<String> myset = mymap.get(finalDate);
                if (myset==null){
                    myset = new HashSet<>();
                    mymap.put(finalDate, myset);
                }
                while(count<19) {
                    String tempToken = myline.nextToken();
                    myset.add(tempToken);
                    //System.out.print(tempToken + "   ");
                    count++;
                }
                //System.out.println(myline[13]+space+myline[14]+space+myline[15]+space+myline[16]+space+myline[17]+space
                //      +myline[18]+space+myline[19]+space+myline[20]);
                //System.out.println(myline.length);
            }
            fileReader.close();
            System.out.println(numOfLines);
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[] normalTemp = {"00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
                "14", "15", "16", "20", "21", "22", "23", "30", "31", "36"};

        String[] moderateRain = {"24", "25", "52","53", "59", "62", "63", "67", "81","84", "92"};
        String[] severeRain =  {"55","54","57","64","65","69","82"};

        String[] moderateSnow = {"26", "27","38" , "72", "73","76","77", "86","87","88","94"};
        String[] severeSnow = {"37", "39", "74", "75","78","79","90"};

        String[] moderateOthers = {"09","18","19","28","43","45","46","47","48","49","95", "96"};
        String[] severeOthers = {"17","29","33","34","35","97","98","99"};


        PrintWriter consolidatedWeatherFile = null;
        PrintWriter normalWeatherFile = null;
        PrintWriter moderateRainFile = null;
        PrintWriter severeRainFile = null;
        PrintWriter moderateSnowFile = null;
        PrintWriter severeSnowFile = null;
        PrintWriter moderateOthersFile = null;
        PrintWriter severeOthersFile = null;
        try {
            consolidatedWeatherFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            (fileToWrite)), "UTF-8"));
            normalWeatherFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/normalWeatherFile.txt")), "UTF-8"));
            moderateRainFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/moderateRainFile.txt")), "UTF-8"));
            severeRainFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/severeRainFile.txt")), "UTF-8"));
            moderateSnowFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/moderateSnowFile.txt")), "UTF-8"));
            severeSnowFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/severeSnowFile.txt")), "UTF-8"));
            moderateOthersFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/moderateOthersFile.txt")), "UTF-8"));
            severeOthersFile = new PrintWriter(new OutputStreamWriter(
                    new BufferedOutputStream(new FileOutputStream
                            ("/home/kashishdua/Downloads/Big Data project/severeOthersFile.txt")), "UTF-8"));

            //we can now assume that one date time period will come only once due to previous step processing
            for (String s : mymap.keySet()) {
                HashSet<String> tempSet = mymap.get(s);
                boolean testNormalWeather = true;
                for (String test : moderateRain) {
                    if (tempSet.contains(test) == true) {
                        List<String> temp = consolidatedWeatherMap.get(s);
                        if(temp==null){
                            temp = new ArrayList<String>();
                            temp.add("ModerateRain");
                            consolidatedWeatherMap.put(s, temp);
                        }
                        else{
                            temp.add("ModerateRain");
                        }
                        //write to moderate rain list
                        moderateRainList.add(s);
                        testNormalWeather = false;
                        break;
                    }
                }

                for (String test : severeRain) {
                    if (tempSet.contains(test) == true) {
                        List<String> temp = consolidatedWeatherMap.get(s);
                        if(temp==null){
                            temp = new ArrayList<String>();
                            temp.add("SevereRain");
                            consolidatedWeatherMap.put(s, temp);
                        }
                        else{
                            temp.add("SevereRain");
                        }
                        //write to severe rain list
                        severeRainList.add(s);
                        testNormalWeather = false;
                        break;
                    }
                }

                for (String test : moderateSnow) {
                    if (tempSet.contains(test) == true) {
                        List<String> temp = consolidatedWeatherMap.get(s);
                        if(temp==null){
                            temp = new ArrayList<String>();
                            temp.add("ModerateSnow");
                            consolidatedWeatherMap.put(s, temp);
                        }
                        else{
                            temp.add("ModerateSnow");
                        }
                        //write to moderate snow list
                        moderateSnowList.add(s);
                        testNormalWeather = false;
                        break;
                    }
                }

                for (String test : severeSnow) {
                    if (tempSet.contains(test) == true) {
                        List<String> temp = consolidatedWeatherMap.get(s);
                        if(temp==null){
                            temp = new ArrayList<String>();
                            temp.add("SevereSnow");
                            consolidatedWeatherMap.put(s, temp);
                        }
                        else{
                            temp.add("SevereSnow");
                        }
                        //write to severe snow list
                        severeSnowList.add(s);
                        testNormalWeather = false;
                        break;
                    }
                }

                for (String test : moderateOthers) {
                    if (tempSet.contains(test) == true) {
                        List<String> temp = consolidatedWeatherMap.get(s);
                        if(temp==null){
                            temp = new ArrayList<String>();
                            temp.add("ModerateOthers");
                            consolidatedWeatherMap.put(s, temp);
                        }
                        else{
                            temp.add("ModerateOthers");
                        }
                        //write to moderate others file
                        moderateothersList.add(s);
                        testNormalWeather = false;
                        break;
                    }
                }

                for (String test : severeOthers) {
                    if (tempSet.contains(test) == true) {
                        List<String> temp = consolidatedWeatherMap.get(s);
                        if(temp==null){
                            temp = new ArrayList<String>();
                            temp.add("SevereOthers");
                            consolidatedWeatherMap.put(s, temp);
                        }
                        else{
                            temp.add("SevereOthers");
                        }
                        //write to severe rain file
                        severeothersList.add(s);
                        testNormalWeather = false;
                        break;
                    }
                }

                if(testNormalWeather) {
                    List<String> temp = consolidatedWeatherMap.get(s);
                    if(temp==null){
                        temp = new ArrayList<String>();
                        temp.add("Normal");
                        consolidatedWeatherMap.put(s, temp);
                    }
                    else{
                        temp.add("Normal");
                    }
                    //write to normal weather list
                    normalWeatherList.add(s);

                }
            }

            //making a consolidated list
            Set set = consolidatedWeatherMap.entrySet();
            Iterator iterator = set.iterator();
            while(iterator.hasNext()){
                Map.Entry<String, List<String>> map = (Map.Entry)iterator.next();
                String date = map.getKey()+" ";
                List<String> temp = map.getValue();
                for(String s:temp)
                    date = date+"/"+s;

                consolidatedWeatherList.add(date);
            }

            Collections.sort(consolidatedWeatherList);
//            Collections.sort(normalWeatherList);
//            Collections.sort(moderateRainList);
//            Collections.sort(severeRainList);
//            Collections.sort(moderateSnowList);
//            Collections.sort(severeSnowList);
//            Collections.sort(moderateothersList);
//            Collections.sort(severeothersList);
//
//            for (String s: normalWeatherList)
//                normalWeatherFile.println(s);
//
//            for (String s: moderateRainList)
//                moderateRainFile.println(s);
//
//            for (String s: severeRainList)
//                severeRainFile.println(s);
//
//            for (String s: moderateSnowList)
//                moderateSnowFile.println(s);
//
//            for (String s: severeSnowList)
//                severeSnowFile.println(s);

//            for (String s: moderateothersList)
//                moderateOthersFile.println(s);

//            for (String s: severeothersList)
//                severeOthersFile.println(s);
            String temp = "";
            for(int i=0;i<8760;i++){
                temp = consolidatedWeatherList.get(i);
                consolidatedWeatherFile.print(temp+"\n");
                temp = null;
            }



            System.out.println(consolidatedWeatherList.size());
            System.out.println(consolidatedWeatherList.get(8758));
            System.out.println(consolidatedWeatherList.get(8759));
            /*
            display(normalWeatherList, "Normal Weather");
            display(moderateRainList, "Moderate Rain");
            display(severeRainList, "Severe Rain");
            display(moderateSnowList, "Moderate Snow");
            display(severeSnowList, "Severe Snow");
            display(moderateothersList, "Moderate Other Weather");
            display(severeothersList, "Severe Other Weather");
            */

        }catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }finally {
            normalWeatherFile.flush();
            normalWeatherFile.close();
            moderateRainFile.flush();
            moderateRainFile.close();
            severeRainFile.flush();
            severeRainFile.close();
            moderateSnowFile.flush();
            moderateSnowFile.close();
            severeSnowFile.flush();
            severeSnowFile.close();
            moderateOthersFile.flush();
            moderateOthersFile.close();
            severeOthersFile.flush();
            severeOthersFile.close();
        }
    }
    private static void display(List<String> list, String type){
        if (list.size()!=0) {
            for (String s : list) {
                System.out.println(s + "  " + type);
            }
            System.out.println();
        }
    }
}