(this.webpackJsonptodo=this.webpackJsonptodo||[]).push([[0],[,,,,,,,,,,,,,,,,function(e,t,n){},function(e,t,n){},,function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},,function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){"use strict";n.r(t);var c=n(2),a=n.n(c),s=n(7),i=n.n(s),r=(n(16),n(3)),o=(n(17),n(1));function l(){var e=Object(c.useState)(new Date),t=Object(r.a)(e,2),n=t[0],a=t[1];return Object(c.useEffect)((function(){var e=setInterval((function(){return a(new Date)}),1e3);return function(){clearInterval(e)}}),[]),Object(o.jsxs)(o.Fragment,{children:[Object(o.jsx)("div",{className:"box-element clock-container",children:n.toDateString()}),Object(o.jsxs)("p",{className:"time",children:[" ",n.toLocaleTimeString()," "]})]})}n(19);var j=function(e){return Object(o.jsxs)("div",{className:"animation-area",children:[Object(o.jsxs)("ul",{className:"box-area",children:[Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{}),Object(o.jsx)("li",{})]}),e.children]})},d=(n(20),function(){return Object(o.jsxs)("div",{style:{height:"100%"},children:[Object(o.jsx)("div",{className:"nav-container",children:Object(o.jsx)("h1",{children:"TODO APP"})}),Object(o.jsx)("hr",{})]})}),u=(n(21),n(22),n(5)),b=n.n(u),h=n(8),O={url:"https://sarfaraj4444.pythonanywhere.com"};function m(){return(m=Object(h.a)(b.a.mark((function e(t,n){var c,a,s,i=arguments;return b.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return c=i.length>2&&void 0!==i[2]?i[2]:"",e.next=3,fetch(O.url+t);case 3:return a=e.sent,e.next=6,a.json();case 6:return s=e.sent,n(s),c&&c(0),"token"in s&&localStorage.setItem("taskToken",s.token),e.abrupt("return",0);case 11:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function x(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"",c=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"",a=arguments.length>4&&void 0!==arguments[4]?arguments[4]:"";t.token=localStorage.getItem("taskToken");var s={"Content-Type":"application/json"};null!==localStorage.getItem("Token")&&(s.Authorization="Token "+localStorage.getItem("Token"));var i={method:"POST",headers:s,body:JSON.stringify(t)};fetch(O.url+e,i).then((function(e){return e.json()})).then((function(e){n&&n(e),c&&c(0),a&&a()}))}n(24);var f=n(9),v=function(e){var t=e.task;return t.done?Object(o.jsx)(f.a,{color:"rgb(0, 255, 0)"}):Object(o.jsx)("input",{className:"checkbox",type:"checkbox",name:"task"+String(t.id),onClick:function(t){var n=localStorage.getItem("taskToken");t.target.checked?(t.target.checked=!1,x("/todo/complete/",{token:n,id:e.task.id},e.setdata),setTimeout(e.setstate(e.index+10),400)):document.getElementById(p).style.textDecoration="none"}})},g=function(e){return Object(o.jsx)("div",{className:"list-container",children:e.list.map((function(t,n){var c=200*n+200-40*n;c>7e3&&(c=7e3);var a=String(c)+"ms";return Object(o.jsxs)("div",{className:"list-item",style:{animationDuration:a},children:[Object(o.jsxs)("div",{style:{background:"none"},children:[Object(o.jsx)(v,{setdata:e.setdata,task:t})," "]}),Object(o.jsx)("p",{children:t.task})]})}))})},k=(n(25),function(e){var t=Object(c.useState)(""),n=Object(r.a)(t,2),a=n[0],s=n[1];return Object(o.jsxs)("form",{onSubmit:function(t){t.preventDefault();var n={task:a};s(""),document.getElementById("todo").selected="selected",e.refresh(0),x("/todo/post/",n,e.setdata)},className:"form-container",children:[Object(o.jsx)("input",{type:"text",required:!0,value:a,onChange:function(e){s(e.target.value)},name:"task",placeholder:"New Task"}),Object(o.jsx)("input",{type:"submit",value:"Add Task"})]})}),S=function(){var e=Object(c.useState)(0),t=Object(r.a)(e,2),n=t[0],a=t[1],s=Object(c.useState)({tasks:[]}),i=Object(r.a)(s,2),l=i[0],j=i[1];Object(c.useEffect)((function(){var e="create";null!==localStorage.getItem("taskToken")&&(e=localStorage.getItem("taskToken")),function(e,t){m.apply(this,arguments)}("/todo/get/"+String(n)+"/"+e+"/",j)}),[n]);return Object(o.jsxs)("div",{className:"any-container content-container",children:[Object(o.jsx)(k,{setdata:j,refresh:a,type:n}),Object(o.jsx)("div",{id:"lisType",children:Object(o.jsxs)("select",{onChange:function(e){console.log(e.target.value),j({tasks:[]}),a(e.target.value)},children:[Object(o.jsx)("option",{id:"todo",value:0,children:"TODO"}),Object(o.jsx)("option",{value:1,children:"Complete Task"})]})}),Object(o.jsx)(g,{list:l.tasks,setdata:j})]})},N=n(6),y=n(10),T=n(11);n(26);function w(){return Object(o.jsxs)("div",{className:"footer-container",children:[Object(o.jsxs)("div",{className:"tag",children:["@2021 Sarfarajansari ",Object(o.jsx)("hr",{})]}),Object(o.jsx)("p",{style:{textAlign:"center",fontSize:"2rem",marginBottom:"1rem",color:"white"},children:"Social"}),Object(o.jsxs)("div",{className:"social-item",children:[Object(o.jsxs)("a",{href:"https://twitter.com/Sarfraj49393426",children:[Object(o.jsx)(N.b,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Twitter"})]}),Object(o.jsxs)("a",{href:"https://www.instagram.com/sarfarajansari_/",children:[Object(o.jsx)(y.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Instagram"})]}),Object(o.jsxs)("a",{href:"https://github.com/sarfarajansari",children:[Object(o.jsx)(N.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"Github"})]}),Object(o.jsxs)("a",{href:"https://www.linkedin.com/in/sarfaraj-ansari-a0a9441b9/",children:[Object(o.jsx)(T.a,{className:"social-icon main"}),Object(o.jsx)("div",{className:"social-name",children:"LinkedIn"})]})]})]})}var I=function(){return Object(o.jsx)(o.Fragment,{children:Object(o.jsx)(j,{children:Object(o.jsxs)("div",{id:"grid",children:[Object(o.jsxs)("div",{id:"navbar",children:[Object(o.jsx)(d,{})," "]}),Object(o.jsxs)("div",{id:"content",children:[Object(o.jsx)(l,{}),Object(o.jsx)(S,{})]}),Object(o.jsxs)("div",{id:"footer",children:[Object(o.jsx)("hr",{}),Object(o.jsx)(w,{}),"  "]})]})})})},D=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,28)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,s=t.getLCP,i=t.getTTFB;n(e),c(e),a(e),s(e),i(e)}))};i.a.render(Object(o.jsx)(a.a.StrictMode,{children:Object(o.jsx)(I,{})}),document.getElementById("root")),D()}],[[27,1,2]]]);
//# sourceMappingURL=main.8c1e6d7d.chunk.js.map