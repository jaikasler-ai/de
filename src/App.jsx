import React, { useState } from 'react';
import { INITIAL_SUBJECTS, INITIAL_QUESTIONS, INITIAL_MISTAKES } from './data/mockData';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import DashboardView from './components/DashboardView';
import SubjectsView from './components/SubjectsView';
import BankView from './components/BankView';
import PdfImportView from './components/PdfImportView';
import MistakesView from './components/MistakesView';
import StatsView from './components/StatsView';
import QuizEngine from './components/QuizEngine';
import UEConfigModal from './components/UEConfigModal';
import QuestionModal from './components/QuestionModal';
import LoginView from './components/LoginView';

export default function App() {
  const [currentView, setCurrentView] = useState('dashboard');
  const [isAuthenticated, setIsAuthenticated] = useState(true);
  const [user, setUser] = useState({ 
    name: 'Dr. Alexis Martin', 
    email: 'alexis.m@med-prep.io', 
    xp: 2450, 
    level: 12, 
    streak: 5 
  });
  
  const [subjects, setSubjects] = useState(INITIAL_SUBJECTS);
  const [questions, setQuestions] = useState(INITIAL_QUESTIONS);
  const [mistakes, setMistakes] = useState(INITIAL_MISTAKES);

  // Bank Filter and Management States
  const [selectedBankSubject, setSelectedBankSubject] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [showQuestionModal, setShowQuestionModal] = useState(false);
  const [editingQuestion, setEditingQuestion] = useState(null);
  const [questionForm, setQuestionForm] = useState({
    subjectId: 'sub-1',
    chapter: 'Fiche n°1 - Introduction à la Biologie moléculaire.pdf',
    year: 2026,
    difficulty: 'Moyen',
    tags: '',
    statement: '',
    answers: [
      { text: '', correct: false },
      { text: '', correct: false },
      { text: '', correct: false },
      { text: '', correct: false }
    ],
    explanation: ''
  });

  const [isExtractingAI, setIsExtractingAI] = useState(false);

  // Active Quiz State
  const [activeQuizMode, setActiveQuizMode] = useState(null); // 'training', 'crashtest', 'mistakes'
  const [quizQuestions, setQuizQuestions] = useState([]);
  const [currentQuizIndex, setCurrentQuizIndex] = useState(0);
  const [quizScore, setQuizScore] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [quizFinished, setQuizFinished] = useState(false);
  const [userAnswersHistory, setUserAnswersHistory] = useState([]);

  // UE Config Modal State (Série QCM vs Crash Test avec Cœurs : 1, 3, 5)
  const [showUEConfigModal, setShowUEConfigModal] = useState(false);
  const [selectedSubjectForQuiz, setSelectedSubjectForQuiz] = useState(null);
  const [selectedChapterForQuiz, setSelectedChapterForQuiz] = useState(null);
  const [quizLaunchMode, setQuizLaunchMode] = useState('training'); // 'training' or 'crashtest'
  const [crashTestHearts, setCrashTestHearts] = useState(3); // 1, 3, or 5 hearts
  const [remainingHearts, setRemainingHearts] = useState(3);

  // Selected UE detail view for chapters
  const [selectedDetailedSubject, setSelectedDetailedSubject] = useState(null);

  const openUEConfig = (subject, chapter = null) => {
    setSelectedSubjectForQuiz(subject);
    setSelectedChapterForQuiz(chapter);
    setShowUEConfigModal(true);
  };

  const launchConfiguredQuiz = () => {
    setShowUEConfigModal(false);
    let pool = questions.filter(q => q.subjectId === selectedSubjectForQuiz.id);
    if (selectedChapterForQuiz) {
      pool = pool.filter(q => q.chapter === selectedChapterForQuiz);
    }
    if (pool.length === 0) {
      pool = questions.filter(q => q.subjectId === selectedSubjectForQuiz.id);
    }
    if (pool.length === 0) {
      pool = [...questions];
    }
    pool.sort(() => Math.random() - 0.5);
    setQuizQuestions(pool);
    setCurrentQuizIndex(0);
    setQuizScore(0);
    setSelectedAnswer(null);
    setQuizFinished(false);
    setUserAnswersHistory([]);
    setActiveQuizMode(quizLaunchMode);
    if (quizLaunchMode === 'crashtest') {
      setRemainingHearts(crashTestHearts);
    }
  };

  const startQuiz = (mode, subjectId = null) => {
    let pool = [...questions];
    if (subjectId) {
      pool = pool.filter(q => q.subjectId === subjectId);
    }
    if (mode === 'mistakes') {
      const mistakeIds = mistakes.map(m => m.questionId);
      pool = pool.filter(q => mistakeIds.includes(q.id));
      if (pool.length === 0) {
        alert("Aucune erreur enregistrée dans votre Coin Faute ! Bravo.");
        return;
      }
    }
    if (pool.length === 0) {
      alert("Aucune question disponible pour cette sélection.");
      return;
    }
    pool.sort(() => Math.random() - 0.5);
    setQuizQuestions(pool);
    setCurrentQuizIndex(0);
    setQuizScore(0);
    setSelectedAnswer(null);
    setQuizFinished(false);
    setUserAnswersHistory([]);
    setActiveQuizMode(mode);
    if (mode === 'crashtest') {
      setRemainingHearts(3);
    }
  };

  const handleAnswerSubmit = (ansIndex) => {
    if (selectedAnswer !== null) return;
    setSelectedAnswer(ansIndex);
    const currentQ = quizQuestions[currentQuizIndex];
    const isCorrect = currentQ.answers[ansIndex].correct;

    setUserAnswersHistory(prev => [...prev, {
      question: currentQ,
      selectedAnswerIndex: ansIndex,
      isCorrect
    }]);

    if (isCorrect) {
      setQuizScore(prev => prev + 1);
    } else {
      if (!mistakes.some(m => m.questionId === currentQ.id)) {
        setMistakes(prev => [
          ...prev, 
          { 
            id: 'm-' + Date.now(), 
            questionId: currentQ.id, 
            date: new Date().toISOString().split('T')[0], 
            userChoice: ansIndex, 
            correctChoice: currentQ.answers.findIndex(a => a.correct) 
          }
        ]);
      }
      if (activeQuizMode === 'crashtest') {
        setRemainingHearts(prev => {
          const nextHearts = prev - 1;
          if (nextHearts <= 0) {
            setTimeout(() => {
              setQuizFinished(true);
            }, 1200);
          }
          return nextHearts;
        });
      }
    }
  };

  const nextQuizQuestion = () => {
    if (activeQuizMode === 'crashtest' && remainingHearts <= 0) {
      setQuizFinished(true);
      return;
    }
    if (currentQuizIndex + 1 < quizQuestions.length) {
      setCurrentQuizIndex(prev => prev + 1);
      setSelectedAnswer(null);
    } else {
      setQuizFinished(true);
      setUser(prev => ({ ...prev, xp: prev.xp + (quizScore * 15) + 50 }));
    }
  };

  const changeQuestionSubject = (questionId, newSubjectId) => {
    const targetSub = subjects.find(s => s.id === newSubjectId);
    const defaultChap = targetSub && targetSub.chapters.length > 0 ? targetSub.chapters[0] : 'Général';
    setQuestions(questions.map(q => q.id === questionId ? { ...q, subjectId: newSubjectId, chapter: defaultChap } : q));
  };

  const changeQuestionChapter = (questionId, newChapter) => {
    setQuestions(questions.map(q => q.id === questionId ? { ...q, chapter: newChapter } : q));
  };

  const saveQuestion = (e) => {
    e.preventDefault();
    const formattedAnswers = questionForm.answers.map((a, idx) => ({
      id: String.fromCharCode(97 + idx),
      text: a.text,
      correct: a.correct
    }));

    if (editingQuestion) {
      setQuestions(questions.map(q => q.id === editingQuestion.id ? { 
        ...questionForm, 
        id: q.id, 
        answers: formattedAnswers, 
        tags: typeof questionForm.tags === 'string' ? questionForm.tags.split(',').map(t => t.trim()) : questionForm.tags 
      } : q));
    } else {
      const newQ = {
        ...questionForm,
        id: 'q-' + Date.now(),
        answers: formattedAnswers,
        tags: typeof questionForm.tags === 'string' ? questionForm.tags.split(',').map(t => t.trim()) : questionForm.tags
      };
      setQuestions([newQ, ...questions]);
    }
    setShowQuestionModal(false);
    setEditingQuestion(null);
  };

  const deleteQuestion = (id) => {
    setQuestions(questions.filter(q => q.id !== id));
  };

  const duplicateQuestion = (q) => {
    const dup = { ...q, id: 'q-' + Date.now(), statement: q.statement + ' (Copie)' };
    setQuestions([dup, ...questions]);
  };

  const simulateAIExtraction = () => {
    setIsExtractingAI(true);
    setTimeout(() => {
      setIsExtractingAI(false);
      const generated = {
        id: 'q-' + Date.now(),
        subjectId: subjects[7].id,
        chapter: 'Fiche n°2 - Caractères généraux des enzymes.pdf',
        year: 2026,
        difficulty: 'Moyen',
        tags: ['IA', 'PDF', 'Biochimie'],
        statement: 'Quelle est la définition du turnover (kcat) d’une enzyme ?',
        answers: [
          { id: 'a', text: 'Le nombre de molécules de substrat transformées par site actif et par unité de temps à saturation', correct: true },
          { id: 'b', text: 'L’affinité globale de l’enzyme pour son substrat', correct: false },
          { id: 'c', text: 'La température optimale d’activité', correct: false },
          { id: 'd', text: 'La concentration d’inhibiteur compétitif', correct: false }
        ],
        explanation: 'Le nombre de tour (kcat) exprime la vitesse maximale par site actif divisée par la concentration en enzymes.'
      };
      setQuestions([generated, ...questions]);
      alert("1 nouvelle question extraite et classée dans l'UE 8 - Biochimie avec succès !");
    }, 1500);
  };

  if (!isAuthenticated) {
    return <LoginView setIsAuthenticated={setIsAuthenticated} />;
  }

  if (activeQuizMode) {
    return (
      <QuizEngine
        activeQuizMode={activeQuizMode}
        setActiveQuizMode={setActiveQuizMode}
        quizQuestions={quizQuestions}
        currentQuizIndex={currentQuizIndex}
        quizScore={quizScore}
        selectedAnswer={selectedAnswer}
        quizFinished={quizFinished}
        userAnswersHistory={userAnswersHistory}
        remainingHearts={remainingHearts}
        handleAnswerSubmit={handleAnswerSubmit}
        nextQuizQuestion={nextQuizQuestion}
      />
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex">
      {/* Sidebar */}
      <Sidebar 
        currentView={currentView}
        setCurrentView={setCurrentView}
        setSelectedDetailedSubject={setSelectedDetailedSubject}
        mistakeCount={mistakes.length}
      />

      {/* Main View Container */}
      <div className="flex-1 flex flex-col min-w-0">
        <Header 
          currentView={currentView}
          selectedDetailedSubject={selectedDetailedSubject}
          user={user}
        />

        <main className="flex-1 p-6 md:p-8 overflow-y-auto">
          {currentView === 'dashboard' && (
            <DashboardView 
              subjects={subjects}
              startQuiz={startQuiz}
              openUEConfig={openUEConfig}
              setSelectedDetailedSubject={setSelectedDetailedSubject}
              setCurrentView={setCurrentView}
            />
          )}

          {currentView === 'subjects' && (
            <SubjectsView 
              subjects={subjects}
              selectedDetailedSubject={selectedDetailedSubject}
              setSelectedDetailedSubject={setSelectedDetailedSubject}
              openUEConfig={openUEConfig}
              setSelectedSubjectForQuiz={setSelectedSubjectForQuiz}
              setSelectedChapterForQuiz={setSelectedChapterForQuiz}
              setQuizLaunchMode={setQuizLaunchMode}
              setShowUEConfigModal={setShowUEConfigModal}
              setSelectedBankSubject={setSelectedBankSubject}
              setSearchQuery={setSearchQuery}
              setCurrentView={setCurrentView}
            />
          )}

          {currentView === 'bank' && (
            <BankView 
              questions={questions}
              subjects={subjects}
              selectedBankSubject={selectedBankSubject}
              setSelectedBankSubject={setSelectedBankSubject}
              searchQuery={searchQuery}
              setSearchQuery={setSearchQuery}
              setEditingQuestion={setEditingQuestion}
              setShowQuestionModal={setShowQuestionModal}
              changeQuestionSubject={changeQuestionSubject}
              changeQuestionChapter={changeQuestionChapter}
              deleteQuestion={deleteQuestion}
              duplicateQuestion={duplicateQuestion}
            />
          )}

          {currentView === 'pdf' && (
            <PdfImportView 
              simulateAIExtraction={simulateAIExtraction}
              isExtractingAI={isExtractingAI}
            />
          )}

          {currentView === 'mistakes' && (
            <MistakesView 
              mistakes={mistakes}
              questions={questions}
              startQuiz={startQuiz}
            />
          )}

          {currentView === 'stats' && (
            <StatsView 
              user={user}
              subjects={subjects}
              questions={questions}
            />
          )}
        </main>
      </div>

      {/* Modals */}
      <UEConfigModal 
        showUEConfigModal={showUEConfigModal}
        setShowUEConfigModal={setShowUEConfigModal}
        selectedSubjectForQuiz={selectedSubjectForQuiz}
        selectedChapterForQuiz={selectedChapterForQuiz}
        quizLaunchMode={quizLaunchMode}
        setQuizLaunchMode={setQuizLaunchMode}
        crashTestHearts={crashTestHearts}
        setCrashTestHearts={setCrashTestHearts}
        launchConfiguredQuiz={launchConfiguredQuiz}
      />

      <QuestionModal 
        showQuestionModal={showQuestionModal}
        setShowQuestionModal={setShowQuestionModal}
        questionForm={questionForm}
        setQuestionForm={setQuestionForm}
        saveQuestion={saveQuestion}
        subjects={subjects}
        editingQuestion={editingQuestion}
      />
    </div>
  );
}
