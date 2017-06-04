
console.log("groups loaded");
$(document).ready(function()
{
    // Create Group function
    var createGroup = function ()
    {
        console.log("create group")
        var aliean = "<div id=\"creategrp\">"+
          "<h3> Create Groups </h3> "+
          "<form  class='form-inline create-form'>"+
              '<div class="form-group">'+
            '<label for="groupName">Group Name:</label>'+
              '<input type="text" class="form-control" name="groupName" id="groupName"></div>'+
              '<div class="form-group">'+
                '<label for="groupImage">Upload Image:</label>'+
                '<input type="image" class="form-control" id="groupImage">'+
              '</div>'+
          "</form>"+
        "</div> "



        $("#application").append(aliean);
        $("#application").append("<div id='list-of-img' style=\"display:none;\"></div>")
    }


    // My Groups
    var myGroups = function ()
    {
        $('#allgroups').remove();
        $('#mygroups').remove();
        //$('#creategrp').remove();

        $.ajax({
            url:"http://localhost:1111/mygroups",
            method:"GET",
            data:{"userid":userid},
            success:function(res)
            {
                var RES1 =JSON.parse(res)
                console.log(RES1)

                //my groups
                $('#application').append('<div class="row text-center" id="mygroups">');
                $('#mygroups').append("<h3> My Groups </h3> ");

                for(var i = 0 ; i < Object.keys(RES1["groupnames"]).length ; i++)
                {
                    //console.log(RES1['groupnames'][i])
                    var group_record = "<div class='per col-md-3 col-sm-6 hero-feature'><div class='thumbnail'>";
                    group_record +=  '<img  class="public" value="'+RES1['groupid'][i]+'" src= "/static'+RES1['groupimage'][i]+'">';
                    group_record += '<p>' + RES1['groupnames'][i] + '</p>';

                    // if ( RES1['groupstat'][i] == 1)
                    // {
                        group_record += '<button id="leave" class="leave btn btn-success">Leave</button>';
                    // }
                    //
                    // else
                    // {
                    //     group_record += '<button class="requested btn btn-danger">Requested</button>';
                    // }

                    group_record +='</div>'
                    $('#mygroups').append(group_record);
                }

                $('#application').append('</div>');

            },
            error:function(error,k)
            {
                console.log(error)
                console.log(k)
            }
        });
    }

    //All Groups
    var allGroups = function ()
    {
        $('#allgroups').remove();
        $('#mygroups').remove();
        //$('#creategrp').remove();
        $.ajax({
            url:"http://localhost:1111/allgroups",
            method:"GET",
            data:{ "userid":userid},
            success:function(res)
            {

                console.log(res['data'])
                //all groups
                $('#application').append('<div class="row text-center" id="allgroups" >');
                $('#allgroups').append("<h3> All Groups </h3> ");
                res=res['data'];
                for(var j = 0 ; j < res.length ; j++)
                {
                    var group_record = "<div class='per col-md-3 col-sm-6 hero-feature'><div class='thumbnail'>";
                    group_record +=  '<img id="imgid" class="public" value="'+ res[j][0] +'" src= "/static'+res[j][2] + '">';
                    group_record += '<p>' +res[j][1]   + '</p>';
                    group_record += '<button  class="join btn btn-primary">Join</button>';
                    group_record +='</div>'
                    $('#allgroups').append(group_record);
                }

                $('#application').append('</div>');
            },
            error:function(error,k){
                console.log(error)
                console.log(k)
            }
        });
    }

    //click group menu
    $("#menugroup").click(function()
    {
        console.log("menu pressed")
        $('#application').text("");
        createGroup();
        myGroups();
        allGroups();
    });

    //join action
    $("#application").on("click",".join",function()
    {
        console.log("join action")
        gid = $(this).prev().prev().attr('value');
        console.log("group id to be joined",gid)
        $.ajax({
                    url:"http://localhost:1111/join",
                    method:"GET",
                    data:{ "userid":userid,"groupid":gid },
                    success:function(res)
                    {
                        $('#allgroups').remove();
                        $('#mygroups').remove();
                        $('#creategrp').remove();
                        createGroup();
                        myGroups();
                        allGroups();
                        console.log("DONE Join");
                    }
                });
    })

    //leave  action
    $("#application").on("click",".leave",function()
    {
        console.log("leave action")
        gid = $(this).prev().prev().attr('value');
        console.log("group id",gid)
        $.ajax({
                url:"http://localhost:1111/leave",
                method:"GET",
                data:{ "userid":userid,"groupid":gid },
                success:function(res)
                {
                    $('#allgroups').remove();
                    $('#mygroups').remove();
                    $('#creategrp').remove();
                    createGroup();
                    myGroups();
                    allGroups();
                    console.log("DONE leave");
                }
        });
    });

    // Create group action
    $("#application").on("click","#groupImage",function(e)
    {
        console.log("Create group action")
        e.preventDefault();
        //$(this).next('.create-form').css("display","");
        var groupName = $('#groupName').val();
        //var groupImage = $('#groupImage').val();
        var imlist = ["A01.png","A02.png","A03.png","A04.png","A05.png","B01.png","B02.png","B03.png","B04.png","B05.png","C01.png","C02.png","C03.png","C04.png","C05.png","D01.png","D02.png","D03.png","D04.png","D05.png","E01.png","E02.png","E03.png","E04.png","E05.png","F01.png","F02.png","F03.png","F04.png","F05.png","FA01.png","FA02.png","FA03.png","FA04.png","FA05.png","FB01.png","FB02.png","FB03.png","FB04.png","FB05.png","FC01.png","FC02.png","FC03.png","FC04.png","FC05.png","FD01.png","FD02.png","FD03.png","FD04.png","FD05.png","FE01.png","FE02.png","FE03.png","FE04.png","FE05.png","FG01.png","FG02.png","FG03.png","FG04.png","FG05.png","FH01.png","FH02.png","FH03.png","FH04.png","FH05.png","FI01.png","FI02.png","FI03.png","FI04.png","FI05.png","G01.png","G02.png","G03.png","G04.png","G05.png","H01.png","H02.png","H03.png","H04.png","H05.png","I01.png","I02.png","I03.png","I04.png","I05.png","J01.png","J02.png","J03.png","J04.png","J05.png","K01.png","K02.png","K03.png","K04.png","K05.png","L01.png","L02.png","L03.png","L04.png","L05.png","M01.png","M02.png","M03.png","M04.png","M05.png","Male-Avatar-Bowler-Hat-icon.png","Male-Avatar-Bow-Tie-icon.png","Male-Avatar-Cool-Cap-icon.png","Male-Avatar-Cool-Sunglasses-icon.png","Male-Avatar-Emo-Haircut-icon.png","Male-Avatar-Goatee-Beard-icon.png","Male-Avatar-Hair-icon.png","Male-Avatar-icon.png","Male-Avatar-Mustache-icon.png","N01.png","N02.png","N03.png","N04.png","N05.png","O01.png","O02.png","O03.png","O04.png","O05.png"]
                       $("#list-of-img").css("display","block")
                        for (var i =0  ; i <imlist.length;i++ )
                        {
                            $("#list-of-img").append("<img class=\"profile_picture\"src=\"static/pic/"+ imlist[i] +"\"   width=\"50\">")
                        }
                        $(".profile_picture").click(function(e)
                        {
                            var groupImage = e.target.src.substr(e.target.src.indexOf("/pic/"),e.target.src.length);
                            $("#list-of-img").css("display","none");
                            $.ajax
                            ({
                                url:"http://localhost:1111/create",
                                method:"GET",
                                data:{ "userid":userid,"groupName":groupName,"groupImg":groupImage },
                                success:function(res)
                                {
                                    $('#allgroups').remove();
                                    $('#mygroups').remove();
                                    $('#creategrp').remove();
                                    createGroup();
                                    myGroups();
                                    allGroups();
                                    console.log("DONE create");
                                }
                            });
                        })
    })
});
