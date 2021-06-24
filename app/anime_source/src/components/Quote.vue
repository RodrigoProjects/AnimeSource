<template>
  <section class="relative block h-72">
    <div
      class="absolute top-0 w-full h-full bg-center bg-cover"
      style="
        background-image: url('https://wallpaperaccess.com/full/39033.png?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=2710&amp;q=80');
        opacity: 40%;
      "
    ></div>

    <div
      class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden"
      style="height: 70px;"
    >
      <svg
        class="absolute bottom-0 overflow-hidden"
        xmlns="http://www.w3.org/2000/svg"
        preserveAspectRatio="none"
        version="1.1"
        viewBox="0 0 2560 100"
        x="0"
        y="0"
      >
        <polygon
          class="text-white fill-current"
          points="2560 0 2560 100 0 100"
        ></polygon>
      </svg>
    </div>
  </section>
  <div
    style="position: relative; top: -13em;"
    class="font-bold text-lg mb-2 text-yellow-900 text-center"
  >
    <p
      v-if="quote"
      class="font-black text-yellow-600 text-xl text-center md:text-3xl"
    >
      " {{ quote.quote.replace('"', "'") }} "
    </p>

    <span v-if="quote" class="w-full p-10 text-center font-bold">
      {{ quote.anime }} - {{ quote.character }}
    </span>
  </div>
</template>

<script>
let axios = require("axios");

export default {
  data() {
    return {
      quote: null,
    };
  },
  created: function () {
    axios
      .get("https://animechan.vercel.app/api/random")
      .then((response) => {
        this.quote = response.data;
      })
      .catch((e) => {
        console.log("Erro no get quote " + e);
        this.quote = {
          anime: "Naruto",
          character: "Naruto",
          quote: "I will be the hokage!",
        };
      });
  },
};
</script>

<style>
.quote {
  transform: translateY(-100%);
}
</style>
