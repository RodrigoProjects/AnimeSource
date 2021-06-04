<template>
  <div>>Teste</div>
</template>

<script>
var gdb = require("../utils/graphdb");
export default {
  data() {
    return {
      producers: null,
    };
  },
  mounted:function(){
      console.log(this.producers)
  },
  created: function (id) {
    console.log(id);
    var query = `
    select ?anime ?title ?score ?rating ?status ?nome ?genre where { 
        ?anime ?s :Anime;
            :hasProducer :producer_${id};
            :hasGenre ?genre ;
    		:title ?title ;
      		:rating ?rating ;
      		:status ?status ;
        	:score ?score .
        :producer_${id} :name ?nome.
    } order by DESC(?title)
    `;
    gdb
      .fetchOntobud(query)
      .then((response) => {
        this.producers = response.data.results.bindings.map((d) => {
          return {
            id: d.producer.value.split("#")[1].split("_")[1],
            NAnimes: d.NAnimes.value,
            nome: d.nome.value,
          };
        });
        console.log(this.producers);
      })
      .catch((e) => {
        console.log("Erro no get studios " + e);
      });
  },
};
</script>

<style>
</style>