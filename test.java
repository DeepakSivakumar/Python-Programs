import java.util.*;
class test{
public static void main(String args[])
{
String s1="Independence Day";
String s2="";
//char arr[]=s1.toCharArray();
for(char i:s1.toCharArray()){
if(s1.indexOf(i)==s1.lastIndexOf(i))
{
System.out.println(i);
}}}}