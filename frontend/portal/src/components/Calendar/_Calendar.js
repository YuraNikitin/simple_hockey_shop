// @vue/component
import Api from '@/helpers/api';
import News from '@/components/News/News.vue';
import TimeTable from '@/components/TimeTable/TimeTable.vue';

export default {
    name: 'Calendar',

    components: {
      News,
      TimeTable
    },

    mixins: [],

    props: {},

    data () {

        return {list: []}
    },

    computed: {},

    watch: {},

    created () {

      this.loadData();
    },

    methods: {
      async loadData(){
              let response = null;
      try {
        response = await Api.post({
          url: 'sign-up',
        });
      } catch (error) {
         console.log(error);
      }
      this.list = response;
      console.log(response);
      }
    }
}
