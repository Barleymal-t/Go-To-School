import React from 'react'
// import axios from 'axios';
import {Inject, ScheduleComponent, Day, Week, WorkWeek, Month, Agenda, Resize, DragAndDrop,EventSettingsModel, ResourcesDirective, ResourceDirective} from '@syncfusion/ej2-react-schedule';
import {DataManager, WebApiAdaptor} from '@syncfusion/ej2-data';
// import { error } from 'console';
import useFetch from './useFetch';



const Scheduler = () => {
const {data,error,isLoading} = useFetch('http://127.0.0.1:5000/lessons');
// console.log(data)
// console.log(new Date(2022,10,2,10,0) )

// // const lessons = [for]
//     data.forEach((lesson)=>{
//       console.log(lesson)
//     })
const localData:EventSettingsModel = {
  dataSource: data,
  fields: {
    startTime: { name: 'start_time' },
    endTime: { name: 'end_time' },
    subject: { name: 'course_name' },
    location: { name: 'room_number' },
  }
    
    
  }
  console.log(localData)
//   const remoteData = new DataManager ({
//     url: 'http://127.0.0.1:5000/lessons',
//     adaptor: new WebApiAdaptor(),
//     crossDomain: true
// })

  // const resourceDataSource: Object[] = [
  //   {Name: 'Embedded Systems', Id: 1, GroupId: 1, Color: '#cb6bb2'},
  // ]

  return (
    <ScheduleComponent currentView='Week' selectedDate={new Date(2022,10,3)} eventSettings={localData}>
      {/* <ResourcesDirective>
        <ResourceDirective field='course_id' title='Course Name' name='C Programming' textField='Name' idField='courseId' colorField='Color' allowMultiple={true} dataSource={resourceDataSource}>
        </ResourceDirective>
      </ResourcesDirective> */}
        <Inject services={[Day, Week, WorkWeek, Month, Agenda, Resize, DragAndDrop]} />
    </ScheduleComponent>
  )
}

export default Scheduler