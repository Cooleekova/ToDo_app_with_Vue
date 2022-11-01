<template>
  <v-container>
    <v-row class="mb-3">
      
      <v-col cols="12">
        <h1>What do you want to do?</h1>
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            v-model="newTodo.text"
            :counter="40"
            :rules="newTodo.titleRules"
            label="Text"
            required
          ></v-text-field>

          
          <v-btn
            color="success"
            class="mr-4"
            :disabled="!newTodo.text"
            @click="add"
          >
            Add
          </v-btn>
          <v-btn color="warning" class="mr-4" @click="reset">Clear</v-btn>
        </v-form>
      </v-col>
    </v-row>
    <v-divider></v-divider>
    <v-row>
      <v-col cols="12" v-if="todoList.length">
    
        <v-list>
          <v-list-item-group
            v-model="selected"
            color="deep-purple"
          >
          <v-list-item
            v-for="item in todoList"
            :key="item.id"
            
          >
          
          <v-list-item-icon>
            {{ item.id }}
          </v-list-item-icon>

          <v-list-item-action>
                <v-checkbox
                  :input-value="item.complete"
                  color="deep-purple"
                  @click="updateStatus(item);"
                ></v-checkbox>
              </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>
                <strong>&nbsp; &nbsp;{{ item.text }}</strong>
            </v-list-item-title>
          </v-list-item-content>

              
                <v-btn
                  color="error"
                  class="mr-4"
                  @click="deleteItem(item);"
                >
                  Delete task
                </v-btn>

            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    selected: [],
    newTodo: {
      title: "",
      description: "",
      titleRules: [
        (v) => !!v || "Text is required",
        (v) => (v && v.length <= 40) || "ToDo must be less than 40 characters",
      ],
      complete: false,
      user: 1,
    },
    todoList: [],
    url: "http://localhost:8000/",
  }),
  mounted() {
    // Get
    this.getTodos();
  },
  methods: {
    getTodos() {
      axios.get(`${this.url}?ordering=complete`).then((response) => {
        this.todoList = response.data;
      });
    },
    reset() {
      this.$refs.form.reset();
    },
    add() {
      var data = this.newTodo;
      axios.post(this.url, data).then((response) => {
        console.log(response);
        this.getTodos();
      });
    },
    updateStatus(item) {
      item.complete = !item.complete;
      const url = `${this.url}${item.id}/`;
      var data = {
        complete: item.complete,
      };
      axios.patch(url, data).then((response) => {
        console.log(response);
        this.getTodos();
      });
    },
    deleteItem(item) {
      const url = `${this.url}${item.id}/`;
      axios.delete(url).then((response) => {
        console.log(response);
        this.getTodos();
      });
    }
  },
};
</script>
