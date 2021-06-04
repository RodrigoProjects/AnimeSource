<template>
  <div></div>
</template>

<script>
var gdb = require("../utils/graphdb");
export default {
  data() {
    return {
      studios: null,
    };
  },
  created: function (id) {
    console.log(id);
    var query = `
    select (count(?anime) as ?NAnimes ) ?studio ?nome  where { 
        ?anime ?s :Anime;
             :hasStudio ?studio. 
        ?studio :name ?nome.
    } group by ?studio ?nome
      order by DESC(?NAnimes) 
    `;
    gdb
      .fetchOntobud(query)
      .then((response) => {
        this.studios = response.data.results.bindings.map((d) => {
          return {
            id: d.studio.value.split("#")[1].split("_")[1],
            NAnimes: d.NAnimes.value,
            nome: d.nome.value,
          };
        });
        console.log(this.studios);
      })
      .catch((e) => {
        console.log("Erro no get studios " + e);
      });
  },
};
</script>

<style>
</style>