(this.webpackJsonptodo=this.webpackJsonptodo||[]).push([[0],{15:function(e,t,n){},33:function(e,t,n){},34:function(e,t,n){},36:function(e,t,n){},37:function(e,t,n){},38:function(e,t,n){},39:function(e,t,n){},40:function(e,t,n){},41:function(e,t,n){},53:function(e,t,n){},54:function(e,t,n){"use strict";n.r(t);var a=n(2),c=n.n(a),r=n(19),s=n.n(r),i=(n(32),n(33),n(4)),o=(n(34),n(1));function l(){var e=Object(a.useState)(new Date),t=Object(i.a)(e,2),n=t[0],c=t[1];return Object(a.useEffect)((function(){var e=setInterval((function(){return c(new Date)}),1e3);return function(){clearInterval(e)}}),[]),Object(o.jsxs)(o.Fragment,{children:[Object(o.jsx)("div",{className:"box-element clock-container",children:n.toDateString()}),Object(o.jsxs)("p",{className:"time",children:[" ",n.toLocaleTimeString()," "]})]})}n(36);var j=function(e){return Object(o.jsxs)("div",{className:"animation-area",children:[Object(o.jsxs)("ul",{className:"box-area",children:[Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{})]}),e.children]})},d=(n(37),function(){return Object(o.jsxs)("div",{style:{height:"100%"},children:[Object(o.jsx)("div",{className:"nav-container",children:Object(o.jsx)("h1",{children:"TODO APP"})}),Object(o.jsx)("hr",{})]})}),u=(n(38),n(39),{url:"https://sarfaraj4444.pythonanywhere.com"});function b(e){if(!e.ok)throw Error(e.statusText);return e}function h(e,t,n){var a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"";n([["loading",!0]]),t.token=localStorage.getItem("taskToken");var c={"Content-Type":"application/json"},r={method:"POST",headers:c,body:JSON.stringify(t)};fetch(u.url+e,r).then(b).then((function(e){return e.json()})).then((function(e){a&&a(e),"message"in e?(n([["alert",""]]),setTimeout((function(){var t="message";e.status&&(t=0==e.status?"message":"error"),n([["alert",e.message],["alertType",t],["loading",!1]])}),5)):n([["loading",!1]])})).catch((function(e){n([["alert",""]]),setTimeout((function(){n([["alert","some error occured please refresh!"],["alertType","error"],["loading",!1]])}),5)}))}n(40);var O=n(20),f=function(e){var t=e.task;return t.done?Object(o.jsx)(O.a,{color:"rgb(0, 255, 0)"}):Object(o.jsx)("input",{className:"checkbox",type:"checkbox",name:"task"+String(t.id),onClick:function(t){var n=localStorage.getItem("taskToken");t.target.checked?(t.target.checked=!1,h("/todo/complete/",{token:n,id:e.task.id},e.update,e.setdata)):document.getElementById(p).style.textDecoration="none"}})},m=function(e){return Object(o.jsx)("div",{className:"list-container",children:e.list.map((function(t,n){var a=200*n+200-40*n;a>7e3&&(a=7e3);var c=String(a)+"ms";return Object(o.jsxs)("div",{className:"list-item",style:{animationDuration:c},children:[Object(o.jsxs)("div",{style:{background:"none"},children:[Object(o.jsx)(f,{update:e.update,setdata:e.setdata,task:t})," "]}),Object(o.jsx)("p",{children:t.task})]},"item"+String(n))}))})},x=(n(41),function(e){var t=Object(a.useState)(""),n=Object(i.a)(t,2),c=n[0],r=n[1];return Object(o.jsxs)("form",{onSubmit:function(t){t.preventDefault();var n={task:c};r(""),document.getElementById("todo").selected="selected",e.refresh(0),h("/todo/post/",n,e.update,e.setdata)},className:"form-container",children:[Object(o.jsx)("input",{autoComplete:"off",type:"text",required:!0,value:c,onChange:function(e){r(e.target.value)},name:"task",placeholder:"New Task"}),Object(o.jsx)("input",{type:"submit",value:"Add Task"})]})}),g=n(56),v=(n(15),function(e){return Object(o.jsx)("div",{className:"spinner",children:Object(o.jsx)(g.a,{size:"large",spinning:e.loading})})});var k=function(e){return Object(a.useEffect)((function(){window.onscroll=function(){e.update([["alert",""]])}}),[]),e.alert?Object(o.jsx)("div",{className:"alert "+e.alertType,id:"alert",role:"alert",children:Object(o.jsx)("p",{children:e.alert})}):Object(o.jsx)(o.Fragment,{})},T=function(){var e=function(){var e=Object(a.useState)(0),t=Object(i.a)(e,2),n=(t[0],t[1]);return function(){return n((function(e){return e+1}))}}(),t=Object(a.useState)({loading:!0,alert:"",alertType:""}),n=Object(i.a)(t,2),c=n[0],r=n[1],s=Object(a.useState)(0),l=Object(i.a)(s,2),j=l[0],d=l[1],h=Object(a.useState)({tasks:[]}),O=Object(i.a)(h,2),f=O[0],g=O[1],p=function(e){for(var t=c,n=0;n<e.length;n++)t[e[n][0]]=e[n][1];console.log(t),r(t)};Object(a.useEffect)((function(){return setInterval(e,10)}),[]),Object(a.useEffect)((function(){var e="create";null!==localStorage.getItem("taskToken")&&(e=localStorage.getItem("taskToken")),function(e,t,n){n([["loading",!0]]),fetch(u.url+e).then(b).then((function(e){return e.json()})).then((function(e){0==e.status?(t(e),n([["loading",!1]]),"token"in e&&localStorage.setItem("taskToken",e.token)):(n([["alert",""]]),setTimeout((function(){n([["alert","some error occured please refresh !"],["alertType","error"],["loading",!1]])}),5),"User not found"==e.message&&localStorage.removeItem("taskToken"))})).catch((function(e){n([["alert",""]]),setTimeout((function(){n([["alert","some error occured please refresh! Please check your internet connection"],["alertType","error"],["loading",!1]])}),5)}))}("/todo/get/"+String(j)+"/"+e+"/",g,p)}),[j]);return Object(o.jsxs)(o.Fragment,{children:[Object(o.jsx)(v,{loading:c.loading}),Object(o.jsx)(k,{alert:c.alert,update:p,alertType:c.alertType}),Object(o.jsxs)("div",{className:c.loading?"any-container content-container loading":"any-container content-container",children:[Object(o.jsx)(x,{update:p,setdata:g,refresh:d,type:j}),Object(o.jsx)("div",{id:"lisType",children:Object(o.jsxs)("select",{onChange:function(e){g({tasks:[]}),d(e.target.value)},children:[Object(o.jsx)("option",{id:"todo",value:0,children:"TODO"}),Object(o.jsx)("option",{value:1,children:"Complete Task"})]})}),Object(o.jsx)(m,{update:p,list:f.tasks,setdata:g})]})]})},y=n(14),S=n(26),N=n(27);n(53);function w(){return Object(o.jsxs)("div",{className:"footer-container",children:[Object(o.jsx)("div",{className:"tag",children:"@2021 Sarfarajansari "}),Object(o.jsx)("p",{style:{textAlign:"center",fontSize:"2rem",marginBottom:"1rem",color:"white"},children:"Social"}),Object(o.jsxs)("div",{className:"social-item",children:[Object(o.jsxs)("a",{href:"https://twitter.com/Sarfraj49393426",children:[Object(o.jsx)(y.b,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Twitter"})]}),Object(o.jsxs)("a",{href:"https://www.instagram.com/sarfarajansari_/",children:[Object(o.jsx)(S.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Instagram"})]}),Object(o.jsxs)("a",{href:"https://github.com/sarfarajansari",children:[Object(o.jsx)(y.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Github"})]}),Object(o.jsxs)("a",{href:"https://www.linkedin.com/in/sarfaraj-ansari-a0a9441b9/",children:[Object(o.jsx)(N.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"LinkedIn"})]})]})]})}var I={loading:!1,alert:"",alertType:""},C=c.a.createContext(),D=function(e){var t=Object(a.useState)(I),n=Object(i.a)(t,2),c=n[0],r=n[1];return Object(o.jsx)(C.Provider,{value:[c,r],children:e.children})};var E=function(){return Object(o.jsx)(o.Fragment,{children:Object(o.jsx)(j,{children:Object(o.jsx)(D,{children:Object(o.jsxs)("div",{id:"grid",children:[Object(o.jsxs)("div",{id:"navbar",children:[Object(o.jsx)(d,{})," "]}),Object(o.jsxs)("div",{id:"content",children:[Object(o.jsx)(l,{}),Object(o.jsx)(T,{})]}),Object(o.jsxs)("div",{id:"footer",children:[Object(o.jsx)("hr",{}),Object(o.jsx)(w,{}),"  "]})]})})})})},F=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,57)).then((function(t){var n=t.getCLS,a=t.getFID,c=t.getFCP,r=t.getLCP,s=t.getTTFB;n(e),a(e),c(e),r(e),s(e)}))};s.a.render(Object(o.jsx)(c.a.StrictMode,{children:Object(o.jsx)(E,{})}),document.getElementById("root")),F()}},[[54,1,2]]]);
//# sourceMappingURL=main.fc421eae.chunk.js.map