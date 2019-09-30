using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

namespace united
{
    public class QueryModel
    {
        private readonly List<SearchResult> _searchResults = new List<SearchResult>();
        
        public bool AddSearchResult(string text)
        {
            if (string.IsNullOrEmpty(text))
            {
                return false;
            }
            
            _searchResults.Add(new SearchResult()
            {
                Content = text
            });
            
            return true;
        }

        public void Reset()
        {
            _searchResults.Clear();
        }
        public void RemoveSearchResult(int index)
        {
            _searchResults.RemoveAt(index);
        }

        public List<SearchResult> Results
        {
            get => _searchResults;
        }
        public async Task<string> RunQueryTask()
        {
            string data;
            List<string> returned = new List<string>();
            string baseUrl = "%%URL%%";
            using (HttpClient client = new HttpClient())
            {
                client.BaseAddress = new Uri(baseUrl);
                using (HttpResponseMessage res = await client.GetAsync("/search"))
                using (HttpContent content = res.Content)
                {
                    data = await content.ReadAsStringAsync();
                    if (data == null)
                    {
                        data = "{}";
                    }
                }
            }
            dynamic parsed = JObject.Parse(data);
            var results = parsed.results;
            foreach (var result in results)
                returned.Add((string) result.text);
            return  String.Join(",", returned);
        }
        public class SearchResult
        {
            public string Content { get; set; }
        }
    }
}