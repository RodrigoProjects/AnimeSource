<template>
  <div>
    <div
      class="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5"
    >
      <template v-for="item in studios" :key="item">
        <!--Card 1-->
        <div class="rounded overflow-hidden shadow-lg">
          <img class="w-full" :src="item.photo" alt="Mountain" />
          <div class="px-6 py-4">
            <a :href="'Studios/' + item.id" class="font-bold text-xl mb-2">{{
              item.nome
            }}</a>
            <p class="text-gray-700 text-base">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Voluptatibus quia, nulla! Maiores et perferendis eaque,
              exercitationem praesentium nihil.
            </p>
          </div>
          <div class="px-6 pt-4 pb-2">
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#photography</span
            >
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#travel</span
            >
            <span
              class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >#winter</span
            >
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
var gdb = require("../utils/graphdb");

const axios = require("axios");

export default {
  data() {
    return {
      studios: null,
    };
  },
  created: function () {
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
        this.studios = response.data.results.bindings
          .map((d) => {
            var nome = d.nome.value.replace(" ", "+");
            axios
              .get(
                "http://localhost:8080/serpapi/search.json?q=" +
                  nome +
                  "+studio+logo&tbm=isch&ijn=0&api_key=secret_api_key"
              )
              .then((dat) => {
                console.log(dat);
                return {
                  id: d.studio.value.split("#")[1].split("_")[1],
                  NAnimes: d.NAnimes.value,
                  nome: d.nome.value,
                };
              });
          })
          .catch((e) => {
            console.log("Erro no get studios " + e);
          });
        console.log(this.studios);
      })
      .catch((e) => {
        console.log("Erro no get studios " + e);
      });
  },
};
</script>

<style></style>
