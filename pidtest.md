## Testing the Datacite graphql API 

[Datacite](https://datacite.org/) announced a [pre-release](https://blog.datacite.org/graphql-api-pre-release/) of 
GraphQL API that can query various different PID (persistent identifier) systems. 


[API Guide](https://support.datacite.org/docs/datacite-graphql-api-guide)

The JSON-like query looks like this. GraphQL spec mandates to define the fields you want to retrieve. The following basically says look up the persistent link using DOI and return the title. 

```
{
  dataset(id: "https://doi.org/<your-pid-link>") {
    titles {
      title
    }
  }
}
```
The response will also be a JSON like text. 

Here's a simple [test](request.py) using Python Requests Module. I am sending a GraphQL query to the datacite API endpoint: https://api.datacite.org/graphql. 


My query looks like this. I am interesting to 
find out other related identifiers if they exist. 
 

```
{
  funder(id: "https://doi.org/10.12344/ABCDE") {
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
```

In the reponse (truncated), we can find out the title and the related identifiers: 

```

"titles": [
                {
                  "title": "My Title"
                }
              ],
              "relatedIdentifiers": [
                {
                  "relatedIdentifier": "10.52xxx/xxcadf",
                  "relationType": "IsVersionOf"
                },
                {
                  "relatedIdentifier": "https://website.org/testpage",
                  "relationType": "IsPartOf"
                }
              ],
              "fundingReferences": [
                {
                  "awardNumber": "123412414"
                }
              ]

```

