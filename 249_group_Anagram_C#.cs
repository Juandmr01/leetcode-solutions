public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        // key is a string a nd the vlaue is a list 
        Dictionary<string, List<string>> groups = new();

        foreach (string word in strs) {
            string key = new string(word.OrderBy(c => c).ToArray());

            if (!groups.ContainsKey(key)) {
                // create a new lsit 
                groups[key] = new List<string>();
            }

            groups[key].Add(word);
        }

        return groups.Values
            .Select(group => (IList<string>)group)
            .ToList();
    }
}