<template>
  <section class="relative py-16 bg-gray-300">
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
                  style="max-width: 300px;"
                />
              </div>
            </div>
            <div class="w-full px-4 lg:order-2 lg:text-right lg:self-center">
              <div class="py-6 px-3 mt-32 sm:mt-0"></div>
            </div>
            <br /><br />
            <div class="text-center mt-12 lg:order-3">
              <h3
                class="text-4xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
              >
                {{ producer.nome }}
              </h3>
            </div>
            <div class="w-full px-4 lg:order-3">
              <div class="flex justify-center py-4 lg:pt-4 pt-8">
                <div class="mr-4 p-3 text-center">
                  <span
                    class="text-xl font-bold block uppercase tracking-wide text-gray-700"
                    >{{ total }}</span
                  ><span class="text-sm text-gray-500">{{
                    tipe.toUpperCase()
                  }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-10 py-10 border-t border-gray-300 text-center">
            <div class="flex flex-wrap justify-center">
              <div class="w-full lg:w-9/12 px-4">
                <p class="mb-4 text-lg leading-relaxed text-gray-800">
                  {{ snip }}
                </p>
                <hr />
                <br />
                <Sec-list :tipe="tipe" :id="id" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
var gdb = require("../utils/graphdb");
var axios = require("axios");
import SecList from "../components/SecList.vue";
export default {
  props: {
    tipe: String,
    id: String,
  },
  components: {
    SecList: SecList,
  },
  data() {
    return {
      producer: [],
      photo: "",
      snip: "",
    };
  },

  created() {
    var query =
      `
    select ?nome where {
        :` +
      this.tipe +
      `_` +
      this.id +
      ` :name ?nome.
    }
    `;
    console.log("query: " + query);
    gdb
      .fetchOntobud(query)
      .then(async (response) => {
        this.producer = { nome: response.data.results.bindings[0].nome.value };
        var name = this.producer.nome.replace(" ", "+");
        const g = axios
          .get(
            "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
              name +
              "+" +
              this.tipe +
              "+logo",
            {
              "Content-Type": "application/json",
              Accept: "application/json",
            }
          )
          .then(async (dat) => {
            const g = axios
              .get(
                "https://www.googleapis.com/customsearch/v1?key=AIzaSyDyHq1RRP_qaMuQhQlRMkr7nD5iX6Znayc&cx=b4564266b17feb682&searchType=image&q=" +
                  name +
                  "+studio+logo"
              )
              .then((dat2) => {
                this.photo = dat2.data.items[0].link;
                this.snip = dat.data.items[0].snippet;
              })
              .catch((e) => {
                this.snip = "Unavailable";
                console.log("Erro no get thinger " + e);
                this.photo =
                  "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg";
              });
            await Promise.resolve(g);
          })
          .catch((e) => {
            console.log(e);
            this.snip = "Unavailable";
            this.photo =
              "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg";
          });
        await Promise.resolve(g);
      })

      .catch((e) => {
        this.snip = "Unavailable";
        this.photo =
          "https://www.wpkube.com/wp-content/uploads/2019/02/503-unavailable-error-wpk.jpg";

        console.log("Erro no get studios " + e);
      });
  },
};
</script>
