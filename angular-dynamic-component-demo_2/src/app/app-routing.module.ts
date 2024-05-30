import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { OverviewComponent } from './overview/overview.component';
import { BuildComponent } from './build/build.component';
import { ReportComponent } from './report/report.component';

const routes: Routes = [
  { path: 'overview', component: OverviewComponent },
  { path: 'build', component: BuildComponent },
  { path: 'report', component: ReportComponent },
  { path: '', redirectTo: '/overview', pathMatch: 'full' },
  { path: '**', redirectTo: '/overview' } // Redirect any other route to overview
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
