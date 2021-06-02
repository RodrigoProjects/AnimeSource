const axios = require("axios");
let prefixes = `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX noInferences: <ontotext.com/explicit>
PREFIX skos: <w3.org/2004/02/skos/core#>
PREFIX : <http://www.semanticweb.org/rodrigop/ontologies/2021/3/animes#>
`;

export function fetchOntobud(q) {
  const body = new URLSearchParams();

  body.append("query", prefixes + q);

  const config = {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  };

  return axios.post(
    "http://localhost:7200/repositories/animeSource?query",
    body,
    config
  );
}
/*
export function getGraphDB(query) {
  let q = encodeURI(prefixes + query);
  return axios.get("http://localhost:7200/repositories/animeSource?query=" + q);
}
*/
