<template>
  <section class="relative py-16 bg-gray-300" v-if="anime != null">
    <div class="container mx-auto px-4">
      <div
        class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64"
      >
        <div class="px-6">
          <div class="flex flex-wrap justify-center">
            <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
              <div class="relative">
                <img
                  alt="..."
                  :src="photo"
                  class="shadow-xl rounded-xl h-auto align-middle border-none -m-16 lg:-ml-16"
                  style="max-width: 170px;"
                />
              </div>
            </div>

            <div
              class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center"
            >
              <div class="flex justify-center py-4 lg:pt-4 pt-8">
                <div class="mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ anime.rank }}</span
                  ><span class="text-sm text-gray-500">Rank</span>
                </div>
                <div class="mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ anime.interested_num }}</span
                  ><span class="text-sm text-gray-500">Interested</span>
                </div>
                <div class="lg:mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ anime.popularity }}</span
                  ><span class="text-sm text-gray-500">Popularity</span>
                </div>
              </div>
            </div>
            <div class="w-full lg:w-4/12 px-4 lg:order-1">
              <div class="flex justify-center py-4 lg:pt-4 pt-8">
                <div class="mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ anime.episodes }}</span
                  ><span class="text-sm text-gray-500">Episodes</span>
                </div>
                <div class="mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ anime.favorites }}</span
                  ><span class="text-sm text-gray-500">Favorites</span>
                </div>
                <div class="lg:mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ anime.score }}</span
                  ><span class="text-sm text-gray-500">Score</span>
                </div>
              </div>
            </div>
          </div>
          <br /><br />
          <div class="text-center mt-12">
            <h3
              class="text-4xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
            >
              {{ anime.title }}
            </h3>
            <div
              class="text-sm leading-normal mt-0 mb-2 text-gray-500 font-bold uppercase"
            >
              {{ anime.title_english }} | {{ anime.title_japanese }}
            </div>
            <h5
              class="text-4md font-semibold leading-normal mb-2 text-gray-400 mb-2"
            >
              {{ anime.type }}
            </h5>

            <div class="mb-2 text-gray-700 mt-10">
              <a
                v-for="item in anime.genre"
                :key="item.id"
                :href="'/genre/' + item.id"
              >
                {{ item.value }}&nbsp;
              </a>
            </div>

            <div class="mb-2 text-gray-500">
              {{ anime.rating }}
            </div>
          </div>

          <div class="mt-10 py-10 border-t border-gray-300 text-center">
            <h3
              class="text-xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
            >
              Background
            </h3>
            <div class="flex flex-wrap justify-center">
              <div class="w-full lg:w-9/12 px-4">
                <p class="mb-4 text-lg leading-relaxed text-gray-800">
                  {{ anime.background }}
                </p>
              </div>
            </div>
            <div class="mt-10 py-10 border-t border-gray-300 text-center">
              <AddInfos :id="d" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import AddInfos from "./AddInfos.vue";
var gdb = require("../utils/graphdb");
var axios = require("axios");

export default {
  name: "InfoAnimes",
  components: {
    AddInfos: AddInfos,
  },
  props: {
    d: String,
  },
  data() {
    return {
      anime: null,
      photo: null,
    };
  },
  created() {
    var query =
      `select * where {
	:anime_` +
      this.d +
      ` a :Anime;
              ?o ?p.
}
    `;

    gdb
      .fetchOntobud(query)
      .then(async (response) => {
        var variab = [];
        var f = {};
        response.data.results.bindings.map((d) => {
          if (d.p.value.includes("#")) {
            f = {};
            f[d.o.value.split("#")[1]] = d.p.value.split("#")[1];
            variab.push(f);
          } else {
            f = {};
            f[d.o.value.split("#")[1]] = d.p.value;
            variab.push(f);
          }
        });
        //convert
        this.anime = {};
        for (var i = 0; i < variab.length; i++) {
          this.anime[Object.keys(variab[i])[0]] = Object.values(variab[i])[0];
        }
        var name = this.anime.title.replace(" ", "+");
        const g = axios
          .get(
            "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
              name +
              "+anime+cover"
          )
          .then((dat) => {
            this.photo = dat.data.items[0].link;
          })
          .catch((e) => {
            console.log("Erro no get anime photo " + e);
            this.photo =
              "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg";
          });
        await Promise.resolve(g);
        var query2 =
          `select * where {
:anime_` +
          this.d +
          ` a :Anime;
              :hasGenre ?p.
               ?p :name ?o.
}`;
        const r = gdb
          .fetchOntobud(query2)
          .then(async (ri) => {
            var gens = [];
            var pi = {};
            ri.data.results.bindings.map((u) => {
              pi = {};
              pi["id"] = u.p.value.split("#")[1].split("_")[1];
              pi["value"] = u.o.value;
              gens.push(pi);
            });
            this.anime["genre"] = gens;
          })
          .catch((e) => console.log(e));
        await Promise.all(r);
      })
      .catch((e) => {
        console.log("Erro no get producer " + e);
      });
  },
};
</script>
