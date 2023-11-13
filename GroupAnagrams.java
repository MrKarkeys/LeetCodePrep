class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            char[] val = strs[i].toCharArray();
            Arrays.sort(val);
            String values = new String(val);
            if(!map.containsKey(values)){
                map.put(values, new ArrayList<String>());
            }
            map.get(values).add(strs[i]);
        }
        return new ArrayList<>(map.values());
    }
}