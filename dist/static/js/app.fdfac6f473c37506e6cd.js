webpackJsonp([1],{"0NOo":function(t,e){},"1/oy":function(t,e){},"7qx0":function(t,e){},"9M+g":function(t,e){},D4uH:function(t,e,s){"use strict";var a={},r={name:"icon",props:{name:{type:String,validator:function(t){return!t||t in a||(console.warn('Invalid prop: prop "name" is referring to an unregistered icon "'+t+'".\nPlease make sure you have imported this icon before using it.'),!1)}},scale:[Number,String],spin:Boolean,inverse:Boolean,pulse:Boolean,flip:{validator:function(t){return"horizontal"===t||"vertical"===t}},label:String},data:function(){return{x:!1,y:!1,childrenWidth:0,childrenHeight:0,outerScale:1}},computed:{normalizedScale:function(){var t=this.scale;return t=void 0===t?1:Number(t),isNaN(t)||t<=0?(console.warn('Invalid prop: prop "scale" should be a number over 0.',this),this.outerScale):t*this.outerScale},klass:function(){return{"fa-icon":!0,"fa-spin":this.spin,"fa-flip-horizontal":"horizontal"===this.flip,"fa-flip-vertical":"vertical"===this.flip,"fa-inverse":this.inverse,"fa-pulse":this.pulse}},icon:function(){return this.name?a[this.name]:null},box:function(){return this.icon?"0 0 "+this.icon.width+" "+this.icon.height:"0 0 "+this.width+" "+this.height},ratio:function(){if(!this.icon)return 1;var t=this.icon,e=t.width,s=t.height;return Math.max(e,s)/16},width:function(){return this.childrenWidth||this.icon&&this.icon.width/this.ratio*this.normalizedScale||0},height:function(){return this.childrenHeight||this.icon&&this.icon.height/this.ratio*this.normalizedScale||0},style:function(){return 1!==this.normalizedScale&&{fontSize:this.normalizedScale+"em"}},raw:function(){if(!this.icon||!this.icon.raw)return null;var t=this.icon.raw,e={};return t=t.replace(/\s(?:xml:)?id=(["']?)([^"')\s]+)\1/g,function(t,s,a){var r="fa-"+(n++).toString(16);return e[a]=r,' id="'+r+'"'}),t=t.replace(/#(?:([^'")\s]+)|xpointer\(id\((['"]?)([^')]+)\2\)\))/g,function(t,s,a,r){var n=s||r;return n&&e[n]?"#"+e[n]:t}),t}},mounted:function(){var t=this;if(this.name||0!==this.$children.length){if(!this.icon){var e=0,s=0;this.$children.forEach(function(a){a.outerScale=t.normalizedScale,e=Math.max(e,a.width),s=Math.max(s,a.height)}),this.childrenWidth=e,this.childrenHeight=s,this.$children.forEach(function(t){t.x=(e-t.width)/2,t.y=(s-t.height)/2})}}else console.warn('Invalid prop: prop "name" is required.')},register:function(t){for(var e in t){var s=t[e];s.paths||(s.paths=[]),s.d&&s.paths.push({d:s.d}),s.polygons||(s.polygons=[]),s.points&&s.polygons.push({points:s.points}),a[e]=s}},icons:a},n=870711;var i={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("svg",{class:t.klass,style:t.style,attrs:{version:"1.1",role:t.label?"img":"presentation","aria-label":t.label,x:t.x,y:t.y,width:t.width,height:t.height,viewBox:t.box}},[t._t("default",[t.icon&&t.icon.paths?t._l(t.icon.paths,function(e,a){return s("path",t._b({key:"path-"+a},"path",e,!1))}):t._e(),t._v(" "),t.icon&&t.icon.polygons?t._l(t.icon.polygons,function(e,a){return s("polygon",t._b({key:"polygon-"+a},"polygon",e,!1))}):t._e(),t._v(" "),t.icon&&t.icon.raw?[s("g",{domProps:{innerHTML:t._s(t.raw)}})]:t._e()])],2)},staticRenderFns:[]};var o=s("VU/8")(r,i,!1,function(t){s("0NOo")},null,null);e.a=o.exports},Ddm8:function(t,e){},GfHa:function(t,e){},Id91:function(t,e){},"N+wu":function(t,e){},NHnr:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=s("7+uW"),r={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"bg-primary",attrs:{id:"app"}},[this._m(0),this._v(" "),e("div",{staticClass:"container"},[e("router-view")],1)])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("nav",{staticClass:"navbar navbar-expand-lg navbar-primary bg-primary"},[e("a",{staticClass:"navbar-brand",staticStyle:{color:"white"},attrs:{href:"#"}},[this._v("Encercla")]),this._v(" "),e("button",{staticClass:"navbar-toggler",attrs:{type:"button","data-toggle":"collapse","data-target":"#navbarSupportedContent","aria-controls":"navbarSupportedContent","aria-expanded":"false","aria-label":"Toggle navigation"}},[e("span",{staticClass:"navbar-toggler-icon"})])])}]};var n=s("VU/8")({name:"App"},r,!1,function(t){s("wM1F")},null,null).exports,i=s("/ocq"),o={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"hello"},[e("h1",[this._v(this._s(this.msg))])])},staticRenderFns:[]};s("VU/8")({name:"HelloWorld",data:function(){return{msg:"Welcome to Your Vue.js App"}}},o,!1,function(t){s("qq3a")},"data-v-634646ce",null).exports;var c={user:{authenticated:!1},checkAuth:function(){var t=localStorage.getItem("access_token");this.user.authenticated=!!t},getAuthHeader:function(){return{Authorization:"Bearer "+localStorage.getItem("access_token")}}},l={name:"Login",data:function(){return{email:"",password:"",error:""}},methods:{login:function(){var t=this;this.$http.post("login",{username:this.email,password:this.password}).then(function(e){return t.loginSuccessful(e)}).catch(function(){return t.loginFailed()})},loginSuccessful:function(t){t.data.access_token?(this.error=!1,localStorage.access_token=t.data.access_token,localStorage.refresh_token=t.data.refresh_token,c.user.authenticated=!0,this.$router.replace(this.$route.query.redirect||"/user")):this.loginFailed(t.data.message)},loginFailed:function(t){this.error=t,delete localStorage.token}},updated:function(){}},u={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"login-wrapper border border-light",staticStyle:{"background-color":"rgb(232,77,32)"}},[s("form",{staticClass:"form-signin",on:{submit:function(e){return e.preventDefault(),t.login(e)}}},[s("h2",{staticClass:"form-signin-heading"},[t._v("Please  sign in")]),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputEmail"}},[t._v("Email address")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.email,expression:"email"}],staticClass:"form-control",attrs:{type:"email",id:"inputEmail",placeholder:"Email address",required:"",autofocus:""},domProps:{value:t.email},on:{input:function(e){e.target.composing||(t.email=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputPassword"}},[t._v("Password")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.password,expression:"password"}],staticClass:"form-control",attrs:{type:"password",id:"inputPassword",placeholder:"Password",required:""},domProps:{value:t.password},on:{input:function(e){e.target.composing||(t.password=e.target.value)}}}),t._v(" "),s("button",{staticClass:"btn btn-lg btn-primary btn-block",attrs:{type:"submit"}},[t._v("Sign in")]),t._v(" "),s("span",[t._v(t._s(t.error))])])])},staticRenderFns:[]};var d=s("VU/8")(l,u,!1,function(t){s("Ddm8")},null,null).exports,m={name:"Register",data:function(){return{email:"",password:"",confirmPassword:"",error:""}},computed:{comparePasswords:function(){return this.password===this.confirmPassword||(error="Passwords don't match",!1)}},methods:{register:function(){var t=this;this.$http.post("registration",{username:this.email,password:this.password}).then(function(e){return t.registerSuccessful(e)}).catch(function(){return t.loginFailed()})},registerSuccessful:function(t){t.data.token?(this.error=!1,localStorage.token=t.data.token,this.$store.dispatch("login"),this.$router.replace(this.$route.query.redirect||"/authors")):this.registerFailed(t.data.message)},registerFailed:function(t){this.error=t,this.$store.dispatch("logout"),delete localStorage.token}}},h={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"register-wrapper border border-light"},[s("form",{staticClass:"form-signin",on:{submit:function(e){return e.preventDefault(),t.register(e)}}},[s("h2",{staticClass:"form-signin-heading"},[t._v("Please Register")]),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputEmail"}},[t._v("Email address")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.email,expression:"email"}],staticClass:"form-control",attrs:{type:"email",id:"inputEmail",placeholder:"Email address",required:"",autofocus:""},domProps:{value:t.email},on:{input:function(e){e.target.composing||(t.email=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputPassword"}},[t._v("Password")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.password,expression:"password"}],staticClass:"form-control",attrs:{type:"password",id:"inputPassword",placeholder:"Password",required:""},domProps:{value:t.password},on:{input:function(e){e.target.composing||(t.password=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"confirmInputPassword"}},[t._v("Password")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.confirmPassword,expression:"confirmPassword"}],staticClass:"form-control",attrs:{type:"password",id:"confirmInputPassword",placeholder:"Confirm Password",required:""},domProps:{value:t.confirmPassword},on:{input:function(e){e.target.composing||(t.confirmPassword=e.target.value)}}}),t._v(" "),s("button",{staticClass:"btn btn-lg btn-primary btn-block",attrs:{type:"submit"}},[t._v("Register")]),t._v(" "),s("span",[t._v(t._s(t.error))])])])},staticRenderFns:[]};var p=s("VU/8")(m,h,!1,function(t){s("N+wu")},"data-v-17388608",null).exports,f=s("WIDu"),v=s.n(f),g={name:"RegisterCompany",data:function(){return{sectors:[],sector:"",subsector:"",comercial_name:"",fiscal_name:"",nif:"",number_survey:"",duplication_survey:"",name_surname:"",telephone_number:"",description:"",comarca:"",territori_leader:"",number_workers:"",error:""}},computed:{sectorCategories:function(){return v()(this.sectors.map(function(t){return t.sector}))},subsectorCategories:function(){var t=this;return this.sectors.filter(function(e){return e.sector==t.sector}).map(function(t){return t.subsector})}},methods:{getSectors:function(){var t=this;this.$http.get("sectors",{}).then(function(e){return t.sectors=e.data}).catch(function(){return""})},register:function(){var t=this;this.$http.post("registrationcompany",{sector:this.sector,subsector:this.subsector,commercial_name:this.commercial_name,fiscal_name:this.fiscal_name,nif:this.nif,duplication_survey:this.duplication_survey,name_surname:this.name_surname,telephone_number:this.telephone_number,description:this.description,comarca:this.comarca,territori_leader:this.territori_leader,number_workers:this.number_workers}).then(function(e){return t.registerSuccessful(e)}).catch(function(){return t.loginFailed()})},registerSuccessful:function(t){t.data.token?(this.error=!1,localStorage.token=t.data.token,this.$store.dispatch("login"),this.$router.replace(this.$route.query.redirect||"/authors")):this.registerFailed(t.data.message)},registerFailed:function(t){this.error=t,this.$store.dispatch("logout"),delete localStorage.token}},mounted:function(){this.getSectors()}},y={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"register-wrapper border border-light"},[s("form",{staticClass:"form-signin",on:{submit:function(e){return e.preventDefault(),t.register(e)}}},[s("h2",{staticClass:"form-signin-heading"},[t._v("Please Register Company")]),t._v(" "),s("div",{staticClass:"form-group"},[s("select",{directives:[{name:"model",rawName:"v-model",value:t.sector,expression:"sector"}],staticClass:"custom-select",on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.sector=e.target.multiple?s:s[0]}}},t._l(t.sectorCategories,function(e){return s("option",[t._v(" \n    "+t._s(e)+"\n  ")])}))]),t._v(" "),t.sector?s("div",{staticClass:"form-group"},[s("select",{directives:[{name:"model",rawName:"v-model",value:t.subsector,expression:"subsector"}],staticClass:"form-control",on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.subsector=e.target.multiple?s:s[0]}}},t._l(t.subsectorCategories,function(e){return s("option",[t._v(" \n    "+t._s(e)+"\n  ")])}))]):t._e(),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputcommercial_name"}},[t._v("commercial_name ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.commercial_name,expression:"commercial_name"}],staticClass:"form-control",attrs:{type:"text",id:"inputcommercial_name",placeholder:"Commercial Name",required:"",autofocus:""},domProps:{value:t.commercial_name},on:{input:function(e){e.target.composing||(t.commercial_name=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputfiscal_name"}},[t._v("fiscal_name ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.fiscal_name,expression:"fiscal_name"}],staticClass:"form-control",attrs:{type:"text",id:"inputfiscal_name",placeholder:"Fiscal Name",required:"",autofocus:""},domProps:{value:t.fiscal_name},on:{input:function(e){e.target.composing||(t.fiscal_name=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputnif"}},[t._v("nif ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.nif,expression:"nif"}],staticClass:"form-control",attrs:{type:"text",id:"inputnif",placeholder:"nif",required:"",autofocus:""},domProps:{value:t.nif},on:{input:function(e){e.target.composing||(t.nif=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputname_surname"}},[t._v("nif ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.name_surname,expression:"name_surname"}],staticClass:"form-control",attrs:{type:"text",id:"inputname_surname",placeholder:"name_surname",required:"",autofocus:""},domProps:{value:t.name_surname},on:{input:function(e){e.target.composing||(t.name_surname=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputtelephone_number"}},[t._v("telephone_number ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.telephone_number,expression:"telephone_number"}],staticClass:"form-control",attrs:{type:"text",id:"inputtelephone_number",placeholder:"telephone_number",required:"",autofocus:""},domProps:{value:t.telephone_number},on:{input:function(e){e.target.composing||(t.telephone_number=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"in\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tputdescription"}},[t._v("description ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.description,expression:"description"}],staticClass:"form-control",attrs:{type:"text",id:"inputdescription",placeholder:"description",required:"",autofocus:""},domProps:{value:t.description},on:{input:function(e){e.target.composing||(t.description=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputcomarca"}},[t._v("comarcan ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.comarca,expression:"comarca"}],staticClass:"form-control",attrs:{type:"text",id:"inputcomarca",placeholder:"comarca",required:"",autofocus:""},domProps:{value:t.comarca},on:{input:function(e){e.target.composing||(t.comarca=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputterritori_leader"}},[t._v("territori_leader ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.territori_leader,expression:"territori_leader"}],staticClass:"form-control",attrs:{type:"text",id:"inputterritori_leader",placeholder:"territori_leader",required:"",autofocus:""},domProps:{value:t.territori_leader},on:{input:function(e){e.target.composing||(t.territori_leader=e.target.value)}}}),t._v(" "),s("label",{staticClass:"sr-only",attrs:{for:"inputnumber_workers"}},[t._v("territori_leader ")]),t._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:t.number_workers,expression:"number_workers"}],staticClass:"form-control",attrs:{type:"text",id:"inputnumber_workers",placeholder:"number_of_workers\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",required:"",autofocus:""},domProps:{value:t.number_workers},on:{input:function(e){e.target.composing||(t.number_workers=e.target.value)}}}),t._v(" "),s("button",{staticClass:"btn btn-lg btn-primary btn-block",attrs:{type:"submit"}},[t._v("Register")]),t._v(" "),s("span",[t._v(t._s(t.error))])])])},staticRenderFns:[]};var b=s("VU/8")(g,y,!1,function(t){s("Yidz")},"data-v-aeb7c2e6",null).exports,w=s("ESch"),C=(s("pYLg"),s("UcI+"),s("R3SC"),s("E8q/")),S=(s("Ea66"),s("EXyZ")),x=s("D4uH"),k={components:{Icon:x.a,"b-button":C.a,"b-tooltip":S.a,"b-modal":w.a},name:"Questions",data:function(){return{msg:"Welcome to Your Vue.js App",questions:[],selected:0,answers:[],company_survey:"",selected_class:"list-group-item-primary",items:[1,2,3,4],timeoutId:""}},computed:{submittable:function(){console.log("sub");var t=[];return this.answers.map(function(e){-1!=e.score&&t.push(e.score)}),this.company_survey.score=t.reduce(function(t,e){return t+e},0),t.length==this.answers.length}},methods:{showModal:function(){this.$refs.myModalRef.show()},hideModal:function(){this.$refs.myModalRef.hide()},onInput:function(t){updateAnswer=this.updateAnswer(),console.log("Textarea Change"),clearTimeout(this.timeoutId),this.timeoutId=setTimeout(function(){this.updateAnswer()},1e3)},submitSurvey:function(){var t=this;this.company_survey.status="submitted";var e=this.company_survey;this.$http.put("companysurvey/"+e.id,{company_survey:e},{headers:c.getAuthHeader()}).then(function(t){console.log("OK")}).catch(function(){return t.company_survey.status="created"})},updateAnswer:function(){var t=this.answers[this.selected];this.$http.put("answer/"+t.id,{answer:t},{headers:c.getAuthHeader()}).then(function(t){console.log("OK")}).catch(function(){return console.log("KO")})},fetchAnswers:function(t){var e=this;this.$http.get("answers?ids="+t,{headers:c.getAuthHeader()}).then(function(t){e.answers=t.data.data}).catch(function(){return""})},fetchQuestions:function(t){var e=this;this.$http.get("questions?ids="+t,{headers:c.getAuthHeader()}).then(function(t){e.questions=t.data.data}).catch(function(){return""})},fetchCompanySurvey:function(){var t=this;this.$http.get("companysurvey/"+this.$route.params.id,{headers:c.getAuthHeader()}).then(function(e){t.company_survey=e.data,t.fetchQuestions(e.data.questions),t.fetchAnswers(e.data.answers)}).catch(function(){return""})},setSelected:function(t){this.selected=t},compare:function(t){return t==this.answers[this.selected].id_option?"background-color:#e84d20; color:white;":"background-color:white; color:black;"},getpoints:function(t,e){var s=2;return""!=t.q3&&(s=3),void 0!=t.q4&&""!=t.q4&&(s=4),e==s?1:1==e?0:2==e&3==s?.5:2==e&4==s?.33:.66},setOption:function(t){this.answers[this.selected].id_option=t,this.answers[this.selected].score=this.getpoints(this.questions[this.selected],t),this.updateAnswer(this.answers[this.selected])},handleFileUpload:function(){var t=this;this.answers[this.selected].justification_file=this.$refs.file.files[0].name;var e=new FormData;e.append("file",this.$refs.file.files[0]),this.$http.post("http://localhost:5000/upload?answer="+this.answers[this.selected].id,e,{headers:{"Content-Type":"multipart/form-data"}}).then(function(e){t.updateAnswer(t.answers[t.selected])}).catch(function(){console.log("FAILURE!!")})}},mounted:function(){this.fetchCompanySurvey()}},q={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"container bg-primary"},[s("div",{staticClass:"row"},[s("div",{staticClass:"col-12"},[t._l(t.questions,function(e,a){return s("li",{staticStyle:{"background-color":"#e84d20"}},[s("span",{on:{click:function(e){t.setSelected(a)}}},[a==t.selected?s("icon",{staticStyle:{height:"1em"},attrs:{name:"circle-o",color:"green"}}):t._e(),t._v(" "),a!=t.selected?s("icon",{staticStyle:{height:"1em"},attrs:{name:"circle-o",color:"black"}}):t._e()],1)])}),t._v(" "),s("h5",{staticClass:"text-left",staticStyle:{color:"white"}},[t._v(t._s(t.questions[t.selected].statement)+"\n    "),s("span",{attrs:{id:"exButton2"}},[s("icon",{staticStyle:{"vertical-align":"middle"},attrs:{name:"question-circle",scale:"1.5"}})],1),t._v(" "),s("div",{staticClass:"container",staticStyle:{"max-width":"100%"},attrs:{id:"dav"}},[s("b-tooltip",{attrs:{boundary:"window",target:"exButton2",placement:"bottom"}},[s("div",{staticClass:"container",staticStyle:{"word-wrap":"break-word",width:"750px","max-height":"500px","font-size":"14px"}},[t._v("\n    "+t._s(t.questions[t.selected].more_information)+"\n    ")])])],1)])],2)]),t._v(" "),s("div",{staticClass:"row"},[s("div",{staticClass:"col-9"},[s("ul",{staticClass:"list-group"},t._l(t.items,function(e){return""!=t.questions[t.selected]["q"+e]?s("li",{staticClass:"list-group-item",style:t.compare(e),on:{click:function(s){t.setOption(e)}}},[t._v(" "+t._s(t.questions[t.selected]["q"+e]))]):t._e()}))])]),t._v(" "),s("div",{staticClass:"row"},[s("div",{staticClass:"col-sm-2"},[s("input",{staticClass:"form-check-input",attrs:{type:"checkbox"}}),t._v("\n            "+t._s(t.answers[t.selected].justification_file)+"\n\t    "),s("label",{staticClass:"form-check-label",attrs:{for:"exampleCheck1"}},[t._v(" Futurible")])]),t._v(" "),s("div",{staticClass:"col-sm-3"},[s("input",{ref:"file",attrs:{type:"file",id:"file"},on:{change:function(e){t.handleFileUpload()}}})])]),t._v(" "),s("div",{staticClass:"row"},[s("div",{staticClass:"col-9"},[s("input",{directives:[{name:"model",rawName:"v-model",value:t.answers[t.selected].justification_text,expression:"answers[selected].justification_text"}],staticClass:"form-control",staticStyle:{height:"100px","background-color":"#e84d20",color:"white"},attrs:{type:"text",id:"inputcommercial_name",placeholder:t.questions[t.selected].futurible,required:"",autofocus:""},domProps:{value:t.answers[t.selected].justification_text},on:{input:[function(e){e.target.composing||t.$set(t.answers[t.selected],"justification_text",e.target.value)},function(e){t.onInput()}]}})])]),t._v(" "),s("div",[s("b-button",{class:{disabled:!t.submittable},attrs:{variant:"success"},on:{click:function(e){t.submitSurvey()}}},[t._v("Submit")])],1)])},staticRenderFns:[]};var $=s("VU/8")(k,q,!1,function(t){s("tae7")},"data-v-73219551",null).exports,A=(s("15Ef"),s("7p6u"),s("dFBv"),s("i71b"),{components:{Icon:x.a},name:"Admin",data:function(){return{msg:"Welcome to Your Vue.js App"}}}),P={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"container"},[e("ul",{staticClass:"list-group"},[e("li",{staticClass:"list-group-item"},[e("a",{attrs:{href:"#/admin/users"}},[this._v("Gestio usuari\n    "),e("icon",{staticStyle:{height:"1em","vertical-align":"middle"},attrs:{name:"user",scale:"4"}})],1)]),this._v(" "),e("li",{staticClass:"list-group-item"},[this._v("Visualitzacio de questionaris\n\t\t"),e("icon",{staticStyle:{height:"1em","vertical-align":"middle"},attrs:{name:"clipboard",scale:"4"}})],1),this._v(" "),e("li",{staticClass:"list-group-item"},[this._v("Ranquing de resultats\n\t\t"),e("icon",{staticStyle:{height:"1em","vertical-align":"middle"},attrs:{name:"line-chart",scale:"4"}})],1),this._v(" "),e("li",{staticClass:"list-group-item"},[this._v("Extraccio d'informes\n\t\t"),e("icon",{staticStyle:{height:"1em","vertical-align":"middle"},attrs:{name:"download",scale:"4"}})],1)])])},staticRenderFns:[]};var R=s("VU/8")(A,P,!1,function(t){s("7qx0")},"data-v-255d52c2",null).exports,F=s("bOdI"),E=s.n(F),I=(s("rcsw"),{components:{Icon:x.a},name:"UsersManagement",data:function(){return{users:[]}},methods:E()({fetchUsers:function(){var t=this;this.$http.get("users",{}).then(function(e){return t.users=e.data.data}).catch(function(){return""})}},"fetchUsers",function(){var t=this;this.$http.get("users",{}).then(function(e){return t.users=e.data.data}).catch(function(){return""})}),mounted:function(){this.fetchUsers()}}),N={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("div",{staticClass:"container bg-primary"},[s("h4",[t._v("List of Users")]),t._v(" "),t._l(t.users,function(e,a){return s("li",[t._v("\n\t"+t._s(e.email)+"\n    ")])}),t._v(" "),s("a",{staticStyle:{color:"white"},attrs:{href:"#/register"}},[t._v(" Add user\n"),s("icon",{staticStyle:{"vertical-align":"middle"},attrs:{name:"plus",scale:"1",color:"white"}})],1)],2),t._v(" "),s("div",{staticClass:"container bg-primary"},[s("h4",[t._v("List of Company")]),t._v(" "),t._l(t.companies,function(e,a){return s("li",[t._v("\n\t"+t._s(t.user.email)+"\n    ")])}),t._v(" "),s("a",{staticStyle:{color:"white"},attrs:{href:"#/registercompany"}},[t._v(" Add company\n"),s("icon",{staticStyle:{"vertical-align":"middle"},attrs:{name:"plus",scale:"1",color:"white"}})],1)],2)])},staticRenderFns:[]};var U=s("VU/8")(I,N,!1,function(t){s("w4C/")},"data-v-68c5f4d1",null).exports,H=(s("h+cp"),{components:{Icon:x.a,"b-modal":w.a},name:"UserPage",data:function(){return{user:"dpiscia",company:{id:1},DARI_filename:"",survey:"",company_surveys:[],error:""}},methods:{fetchCompany:function(){var t=this;this.$http.get("company",{headers:c.getAuthHeader()}).then(function(e){return t.company=e.data}).catch(function(){return""})},fetchSurvey:function(){var t=this;this.$http.get("survey",{headers:c.getAuthHeader()}).then(function(e){return t.survey=e.data}).catch(function(){return""})},fetchCompanySurvey:function(){var t=this;this.$http.get("companysurvey",{headers:c.getAuthHeader()}).then(function(e){return t.company_surveys=e.data}).catch(function(){return""})},DARI_needed:function(){return"Industrial"==this.company.sector||"Agroalimentari"==this.company.sector},createCompanySurvey:function(){var t=this;this.DARI_needed()&&""==this.DARI_filename?this.error="you need to upload a DARI file":this.$http.post("companysurvey",{id_survey:this.survey.id,file_dari:this.DARI_filename,id_company:this.company.id},{headers:c.getAuthHeader()}).then(function(e){return t.registerSuccessful(e)}).catch(function(e){return t.registerFailed(e)})},registerSuccessful:function(t){this.handleFileUpload(t.data.message.split(" ")[2]),this.company_surveys=[],this.fetchCompanySurvey()},registerFailed:function(t){this.error=t.response.data.message},showModal:function(){this.$refs.myModalRef.show()},hideModal:function(){this.$refs.myModalRef.hide()},setFileName:function(){this.DARI_filename=this.$refs.file.files[0].name},handleFileUpload:function(t){this.DARI_filename=this.$refs.file.files[0].name;var e=new FormData;e.append("file",this.$refs.file.files[0]),this.$http.post("http://localhost:5000/upload?surveycompany_id="+t,e,{headers:{"Content-Type":"multipart/form-data"}}).then(function(t){console.log("OK")}).catch(function(){console.log("FAILURE!!")})}},mounted:function(){this.fetchCompany(),this.fetchSurvey(),this.fetchCompanySurvey()}}),M={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"hello"},[s("h4",{staticStyle:{color:"white"}},[t._v(t._s(t.company.commercial_name))]),t._v(" "),s("button",{staticClass:"btn btn-primary",attrs:{type:"button"},on:{click:t.showModal}},[s("icon",{staticStyle:{"vertical-align":"middle"},attrs:{name:"plus-circle",scale:"1.5"}})],1),t._v("Questionari nou\n"),t._v(" "),s("table",{staticClass:"table table-light table-bordered"},[s("thead",[s("tr",[s("th",{attrs:{scope:"col"}},[t._v("Nom questionari")]),t._v(" "),s("th",{attrs:{scope:"col"}},[t._v("Estat")]),t._v(" "),s("th",{attrs:{scope:"col"}},[t._v("Ultima data modificacio")]),t._v(" "),s("th",{attrs:{scope:"col"}},[s("icon",{staticStyle:{height:"1em","vertical-align":"middle"},attrs:{name:"line-chart",scale:"1"}}),t._v("Puntuacio obtinguda")],1)])]),t._v(" "),s("tbody",t._l(t.company_surveys,function(e,a){return s("tr",[s("td",{attrs:{color:"white"}},[s("a",{staticStyle:{color:"black"},attrs:{href:"#/questions/"+e.id}},[t._v(t._s(e.name_survey)+"  ")])]),t._v(" "),s("td",[t._v(t._s(e.status))]),t._v(" "),s("td",[t._v(t._s(e.last_modified))]),t._v(" "),s("td",[s("icon",{staticStyle:{height:"1em"},attrs:{name:"circle",color:"green"}}),t._v("\n       "+t._s(e.score))],1)])}))]),t._v(" "),s("b-modal",{ref:"myModalRef",attrs:{"hide-footer":"",title:""}},[s("div",{staticClass:"d-block text-center"},[s("h3",[t._v("Crear un formulari")]),t._v(" "),1==t.DARI_needed()?s("div",{staticClass:"custom-file"},[s("label",{staticClass:"custom-file-label",attrs:{for:"file"}},[t._v("Adjuntar DARI ")]),t._v(" "),s("input",{ref:"file",staticClass:"form-control-file",attrs:{type:"file",id:"file"},on:{change:function(e){t.setFileName()}}})]):t._e(),t._v("\n      \n      "+t._s(t.error)+"\n      ")]),t._v(" "),s("button",{staticClass:"btn btn-primary",attrs:{variant:"outline-danger",block:""},on:{click:t.hideModal}},[t._v("Cancel")]),t._v(" "),s("button",{staticClass:"btn btn-primary",attrs:{variant:"outline-danger",block:""},on:{click:t.createCompanySurvey}},[t._v("Create")])])],1)},staticRenderFns:[]};var D=s("VU/8")(H,M,!1,function(t){s("VVW1")},"data-v-0590d514",null).exports,V=(s("M4fF"),{name:"Results",data:function(){return{data:[{name:"IE",percent:39.1},{name:"Chrome",percent:32.51},{name:"Safari",percent:13.68},{name:"Firefox",percent:8.71},{name:"Others",percent:6.01}],questions:[],selected:0,answers:[],answerplus:[],company_survey:"",score:"",results_avg:"",results:""}},computed:{},methods:{filtered:function(t){var e=this.questions,s=[];return this.answers.filter(function(a,r){a.score<1&&e[r].strategy==t&&s.push(r)}),s},computeScore:function(){var t;t=this.answers;var e;e=this.questions;var s=[];s=_.map(t,function(t){return _.assign(t,_.find(e,{id:t.id_question}))}).reduce(function(t,e){var s=t[e.strategy];return s?(s.score=s.score+e.score,s.nums=s.nums+1):(t[e.strategy]={score:e.score},t[e.strategy].nums=1),t},{});var a={score:0,numsector:0,avg:0};for(var r in a.score=0,a.numsector=0,s)s[r].avg=s[r].score/s[r].nums,a.score=a.score+s[r].avg,a.numsector=a.numsector+1;this.results=s,a.avg=100*a.score/a.numsector,this.results_avg=a},fetchAnswers:function(t){var e=this;this.$http.get("answers?ids="+t,{headers:c.getAuthHeader()}).then(function(t){e.answers=t.data.data,e.computeScore()}).catch(function(){return""})},fetchQuestions:function(t,e){var s=this;this.$http.get("questions?ids="+t,{headers:c.getAuthHeader()}).then(function(t){s.questions=t.data.data,s.fetchAnswers(e)}).catch(function(){return""})},fetchCompanySurvey:function(){var t=this;this.$http.get("companysurvey/"+this.$route.params.id,{headers:c.getAuthHeader()}).then(function(e){t.company_survey=e.data,t.fetchQuestions(e.data.questions,e.data.answers)}).catch(function(){return""})},renderChart:function(t){var e=d3.layout.pie().value(function(t){return t.percent}).sort(null).padAngle(.03),s=d3.scale.category10(),a=d3.svg.arc().outerRadius(150).innerRadius(100);d3.select("#chart").append("svg").attr({width:300,height:300,class:"shadow"}).append("g").attr({transform:"translate(150,150)"}).selectAll("path").data(e(t)).enter().append("path").attr({d:a,fill:function(t,e){return s(t.data.name)}})}},mounted:function(){this.fetchCompanySurvey(),this.renderChart(this.$data.data)}}),z={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"hello"},[s("div",{staticClass:"container"},[s("div",{staticClass:"col-md-4 offset-md-4",staticStyle:{"background-color":"black","border-radius":"5ex !important"}},[s("p",{staticClass:"text-light"},[t._v(" Punctuacio obtinguda  "+t._s(t.results_avg.avg)+"/100")]),t._v(" "),s("p",{staticClass:"text-light"},[t._v(" Punctuacio futurible  ??/100")])])]),t._v(" "),s("div",{staticClass:"chart",attrs:{id:"chart"}}),t._v(" "),s("p",{staticClass:"text-light"},[t._v("\n\tPropostes de millora per estrategia;\n  ")]),t._v(" "),t._l(t.results,function(e,a){return s("span",{staticClass:"demo"},[s("li",{staticClass:"list-group-item",staticStyle:{color:"#e84d20","border-top-left-radius":"5ex !important","border-top-right-radius":"5ex !important"}},[t._v(t._s(a))]),t._v(" "),t._l(t.filtered(a),function(e,a){return s("li",{staticClass:"list-group-item"},[s("p",[t._v("\n\t\t   "+t._s(t.questions[e].proposta_millora)+"\n\t\t  ")])])}),t._v(" "),s("li",{staticClass:"list-group-item",staticStyle:{"border-bottom-left-radius":"5ex !important","border-bottom-right-radius":"5ex !important"}}),t._v(" "),s("p")],2)})],2)},staticRenderFns:[]};var O=s("VU/8")(V,z,!1,function(t){s("bO23")},"data-v-d05609ae",null).exports,j=s("VU/8")(null,null,!1,null,null,null).exports;a.a.use(i.a);var W=new i.a({routes:[{path:"/",name:"Login",component:d},{path:"/register",name:"Register",component:p,secure:!0},{path:"/registercompany",name:"RegisterCompany",component:b,secure:!0},{path:"/questions/:id",name:"Questions",component:$,secure:!0},{path:"/admin",name:"Admin",component:R,secure:!0},{path:"/admin/users",name:"UsersManagement",component:U,secure:!0},{path:"/user",name:"UserPage",component:D,secure:!0},{path:"/results/:id",name:"Results",component:O,secure:!0},,{path:"/plot/:id",name:"Plot",component:j,secure:!1}]});console.log("interce"),W.beforeEach(function(t,e,s){W.options.routes.forEach(function(e){t.matched[0].path===e.path&&e.secure&&W.app.$http.post("http://localhost:5000/auth/loggedin","data",{headers:c.getAuthHeader()}).catch(function(t){if(200!=t.response.status)return s("/")})}),s()});var L=W,B=s("Rf8U"),T=s.n(B),Q=s("mtWM"),Y=s.n(Q),K=Object({NODE_ENV:"production"}).API_URL||"http://ineditencercla.pythonanywhere.com",G=Y.a.create({baseURL:K,headers:{"Content-Type":"application/json",Authorization:"Bearer "+localStorage.token}});a.a.use(T.a,G);var J=s("e6fC");s("qb6w"),s("9M+g");a.a.config.productionTip=!1,a.a.use(J.a),new a.a({el:"#app",router:L,axios:void 0,components:{App:n},template:"<App/>",http:{root:"http://localhost:5000"}})},VVW1:function(t,e){},Yidz:function(t,e){},bO23:function(t,e){},qb6w:function(t,e){},qq3a:function(t,e){},tae7:function(t,e){},"w4C/":function(t,e){},wM1F:function(t,e){},zj2Q:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.fdfac6f473c37506e6cd.js.map