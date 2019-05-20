import requests

q = """
{
  funder(id: "https://doi.org/10.13039/501100000780") {
    name
    alternateName
    datasets(first: 2) {
      edges {
        relationType
        source
        node {
          id
          titles {
            title
          }
          relatedIdentifiers {
            relatedIdentifier
            relationType
          }
          fundingReferences {
            awardNumber
          }
        }
      }
    }
  }
}
"""

resp = requests.post("https://api.datacite.org/graphql", params={'query': q})
print(resp.text)
