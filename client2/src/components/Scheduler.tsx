import React from 'react'
import {Inject, ScheduleComponent, Day, Week, WorkWeek, Month, Agenda, Resize, DragAndDrop,EventSettingsModel, ResourcesDirective, ResourceDirective} from '@syncfusion/ej2-react-schedule';

const Scheduler = () => {
const localData:EventSettingsModel = {
  dataSource: [{
        EndTime: new Date(2022,10,2,12,0),
        StartTime: new Date(2022,10,2,10,0),
        Subject: 'Testing',
        IsAllDay: true,
        RecurrenceRule: 'FREQ=DAILY; INTERVAL=1; COUNT=10',
    }]
  }

  return (
    <ScheduleComponent currentView='Week' eventSettings={localData}>
      <ResourcesDirective>
        <ResourceDirective field='loginId' title='Course Name' name='C Programming' allowMultiple={true} >

        </ResourceDirective>
      </ResourcesDirective>
        <Inject services={[Day, Week, WorkWeek, Month, Agenda, Resize, DragAndDrop]} />
    </ScheduleComponent>
  )
}

export default Scheduler