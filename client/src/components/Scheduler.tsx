import React from 'react'
import axios from 'axios';
import {Inject, ScheduleComponent, Day, Week, WorkWeek, Month, Agenda, Resize, DragAndDrop,EventSettingsModel, ResourcesDirective, ResourceDirective} from '@syncfusion/ej2-react-schedule';
import { error } from 'console';
import useFetch from './useFetch';



const Scheduler = () => {
const {data,error,isLoading} = useFetch('http://localhost:5000/api/schedule');


const localData:EventSettingsModel = {
  dataSource: [{
        EndTime: new Date(2022,10,2,12,0),
        StartTime: new Date(2022,10,2,10,0),
        Subject: 'Embedded Systems',
        RecurrenceRule: 'FREQ=WEEKLY; INTERVAL=1; COUNT=10',
        courseId: 1
    }]
  }

  const resourceDataSource: Object[] = [
    {Name: 'Embedded Systems', Id: 1, GroupId: 1, Color: '#cb6bb2'},
  ]

  return (
    <ScheduleComponent currentView='Week' eventSettings={localData}>
      <ResourcesDirective>
        <ResourceDirective field='courseId' title='Course Name' name='C Programming' textField='Name' idField='Id' colorField='Color' allowMultiple={true} dataSource={resourceDataSource}>
        </ResourceDirective>
      </ResourcesDirective>
        <Inject services={[Day, Week, WorkWeek, Month, Agenda, Resize, DragAndDrop]} />
    </ScheduleComponent>
  )
}

export default Scheduler