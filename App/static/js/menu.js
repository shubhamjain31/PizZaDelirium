$(document).ready( function (){
    view_menus(); 
   });
 
function view_menus(){
  var uRl = $("#view_menu").attr("data-url");
    table = $('#view_menu').DataTable({
      // "dom": '<"top"i>rt<"bottom"flp><"clear">',
      // "sScrollY": "400px",
  
      "sScrollX": true ,
      select: true,
    dom: 'Blfrtip',
    buttons: [
      {
        "extend": 'csv',
        "text": '<button type="button" class="btn btn-primary btn-sm">Export All</button>',
        "titleAttr": 'csv',
        // "action": newexportaction,
        // "class":"align-items-center"
      },
      // {
      //   text: '<button type="button" class="btn btn-primary">Export</button>',
      //   action: function ( e, dt, node, config ) {
      //   }
      // },
      {
        text: '<button type="button" class="btn btn-primary btn-sm">Import</button>',
        // action: importitems
      },
      // {
      //   text: '<button type="submit" id="delete" class="btn btn-primary btn-sm" style="display:none;">Delete</button>',
      //   // action: deleteaction
      // },
    ],
      "bSort": true,
      "bDestroy": true,
      serverSide: true,
      "processing":true,
      "searching": false,
      "paging": true,
      "order": [],
      "columnDefs": [
        { "orderable": false, "className": 'reorder', "targets": [0] },
        { "targets": [], "orderable": false }
      ],
      "aaSorting": [],
    //   "aLengthMenu": [[2, 25, 100, -1], [2, 25, 100, "All"]],
    //   "iDisplayLength": 2,
      "aLengthMenu": [[10, 25, 100], [10, 25, 100]],
      "iDisplayLength": 10,
      "ajax":{
          url:uRl,
          type:"POST",
          data:{
            // search_contact: $('#view_contacts_search').val(),
          },
        },
      
      dataSrc:"",
  
      columns: [
        { data: null },
        { data: 'category' },
        { data: 'kind', },
        { data: 'price', },
        { data: 'size', },
        {data: 'extra', className: 'text-lowercase'},
        // { "data": "action", className: 'dt-body-right'},
        
    ],
    "oLanguage": {
      "sEmptyTable":     "No Data",
      "sLengthMenu": "_MENU_",
  
  },
  
    "rowCallback": function (nRow, aData, iDisplayIndex) {
        var oSettings = this.fnSettings ();
        $("td:eq(0)", nRow).html(oSettings._iDisplayStart+iDisplayIndex +1);
        return nRow;
   },
    'fnCreatedRow': function (nRow, aData, iDataIndex) {
      $(nRow).attr('id', 'row' + iDataIndex); // or whatever you choose to set as the id
    },
    });
    
  }