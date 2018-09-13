// Author: Grzegorz Tężycki

$(document).ready(function(){

    // In web storage is saved structure like that:
    // localStorage['django_tables2_column_shifter'] = {
    //     'table_class_container1' : {
    //         'id' : 'on',
    //         'col1' : 'off',
    //         'col2' : 'on',
    //         'col3' : 'on',
    //     },
    //     'table_class_container2' : {
    //         'id' : 'on',
    //         'col1' : 'on'
    //     },
    // }

    // main name for key in web storage
    var COLUMN_SHIFTER_STORAGE_ACCESOR = "django_tables2_column_shifter";

    // Return storage structure for shifter
    // If structure does'n exist in web storage
    // will be return empty object
    var get_column_shifter_storage = function(){
        var storage = localStorage.getItem(COLUMN_SHIFTER_STORAGE_ACCESOR);
        if (storage === null) {
            storage = {};
        } else {
            storage = JSON.parse(storage);
        }
        return storage;
    };

    // Save structure in web storage
    var set_column_shifter_storage = function(storage){
        var json_storage = JSON.stringify(storage)
        localStorage.setItem(COLUMN_SHIFTER_STORAGE_ACCESOR, json_storage);
    };

    // Remember state for single button
    var save_btn_state = function($btn){

        // Take css class for container with table
        var table_class_container = $btn.data("table-class-container");
        // Take html object with table
        var $table_class_container = $("#" + table_class_container);
        // Take single button statne ("on" / "off")
        var state = $btn.data("state");
        // td-class is a real column name in table
        var td_class = $btn.data("td-class");
        var storage = get_column_shifter_storage();
        // Table id
        var id = $table_class_container.attr("id");

        // Checking if the ID is already in storage
        if (id in storage) {
            data = storage[id]
        } else {
            data = {}
            storage[id] = data;
        }

        // Save state for table column in storage
        data[td_class] = state;
        set_column_shifter_storage(storage);
    };

    // Load states for buttons from storage for single tabel
    var load_states = function($table_class_container) {
        var storage = get_column_shifter_storage();
        // Table id
        var id = $table_class_container.attr("id");
        var data = {};

        // Checking if the ID is already in storage
        if (id in storage) {
            data = storage[id]

            // For each shifter button set state
            $table_class_container.find(".btn-shift-column").each(function(){
                var $btn = $(this);
                var td_class = $btn.data("td-class");

                // If name of column is in store then get state
                // and set state
                if (td_class in data) {
                    var state = data[td_class]
                    set_btn_state($btn, state);
                }
            });
        }
    };

    // Show table content and hide spiner
    var show_table_content = function($table_class_container){
        $table_class_container.find(".loader").hide();
        $table_class_container.find(".table-wrapper").show();
    };

    // Load buttons states for all button in page
    var load_state_for_all_containters = function(){
        $(".column-shifter-container").each(function(){
            $table_class_container = $(this);

            // Load states for all buttons in single container
            load_states($table_class_container);

            // When states was loaded then table must be show and
            // loader (spiner) must be hide
            show_table_content($table_class_container);
        });
    };

    // change visibility column for single button
    // if button has state "on" then show column
    // else then column will be hide
    shift_column = function( $btn ){
        // button state
        var state = $btn.data("state");

        // td-class is a real column name in table
        var td_class = $btn.data("td-class");
        var table_class_container = $btn.data("table-class-container");
        var $table_class_container = $("#" + table_class_container);
        var $table = $table_class_container.find("table");
        var $cels = $table.find("." + td_class);

        if ( state === "on" ) {
            $cels.show();
        } else {
            $cels.hide();
        }
    };

    // Shift visibility for all columns
    shift_columns = function(){
        var cols = $(".btn-shift-column");
        var i, len = cols.length;
        for (i=0; i < len; i++) {
            shift_column($(cols[i]));
        }
    };

    // Set icon imgae visibility for button state
    var set_icon_for_state = function( $btn, state ) {
        if (state === "on") {
            $btn.find("img.uncheck").hide();
            $btn.find("img.check").show();
        } else {
            $btn.find("img.check").hide();
            $btn.find("img.uncheck").show();
        }
    };

    // Set state for single button
    var set_btn_state = function($btn, state){
        $btn.data('state', state);
        set_icon_for_state($btn, state);
    }

    // Change state for single button
    var change_btn_state = function($btn){
        var state = $btn.data("state");

        if (state === "on") {
            state = "off"
        } else {
            state = "on"
        }
        set_btn_state($btn, state);
    };

    // Run show/hide when click on button
    $(".btn-shift-column").on("click", function(event){
        var $btn = $(this);
        event.stopPropagation();
        change_btn_state($btn);
        shift_column($btn);
        save_btn_state($btn);
    });

    // Load saved states for all tables
    load_state_for_all_containters();

    // show or hide columns based on data from web storage
    shift_columns();
    
    // Add API method for retrieving non-visible cols for table
    // Pass the 0-based index of the table or leave the parameter 
    // empty to return the hidden cols for the 1st table found
    $.django_tables2_column_shifter_hidden = function(idx) {
        if(idx==undefined) {
            idx = 0;
        }
        return $('.table-container').eq(idx).find('.btn-shift-column').filter(function(z) {
            return $(this).data('state')=='off'
        }).map(function(z) { 
            return $(this).data('td-class')
        }).toArray();
    }

});
